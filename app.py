# Tells flask that the entry point of your web app is going to be that file.
# command: export FLASK_APP=app.py export FLASK_DEBUG=true

# Tells Flask to enable the debug mode. (app.py it's the main file of your app)
# command:flask run             in Mac/Linux 
# command: python app.py run   in windows



from flask import Flask, request, jsonify
from flask import Flask, render_template
from db import get_db
from Model import Model
from Controllers.usersController import create_user,get_user,update_user,delete_user,get_all_users,login,verify_token
from Controllers.articlesController import create_article,get_article,update_article,delete_article,get_all_articles
from flask import flash
from flask import make_response
from werkzeug.http import http_date
from datetime import datetime,timezone

app = Flask(__name__)

# set the secret_key for flask app to secure the flash messages
app.secret_key = 'your-secret-key maked it with Sha256'

# init_db() # create the tables if not exists
model_users = Model(get_db(),'users')  # Instance fo Model for connection to database for users
model_articles = Model(get_db(),'articles')  # Instance for Model connection to database for articles
model_tokens = Model(get_db(),'tokens') # Instance for Model connection to database for articles

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/articles', methods=['GET'])
def articles(): 
    if request.method=='GET':
        result=get_all_articles()
        return result
    else:
        return jsonify({'error': 'No articles found'}), 404
        




@app.route('/article', methods=['GET','PUT','DELETE','POST'])
def article():
    # Retrieve the article from the database using model
    # if request.method=='GET':
    #     id=request.form['id']
    #     article = model_articles.read(id)
    #     if not article:
    #         print('not found')
    #     else:
    #         return jsonify(article)
    
    if request.method=='POST':
        data = request.form
        result=create_article(data)
        return result

    if request.method=='PUT':
        data = request.form
        result=update_article(data)
        return result
    if request.method=='DELETE':
        id = request.form['id']
        result=delete_article(id)
        return result

    if request.method=='GET':
        id=request.form['id']
        result=get_article(id)
        return result




@app.route('/user', methods=['GET','PUT','DELETE','POST'])
def user():
    if request.method=='POST':
        data = request.form
        result=create_user(data)
        return result

    if request.method=='PUT':
        data = request.form
        result=update_user(data)
        return result
    if request.method=='DELETE':
        id = request.form['id']
        result=delete_user(id)
        return result

    if request.method=='GET':
        id=request.form['id']
        result=get_user(id)
        return result

@app.route('/userid', methods=['POST'])
def userId():
    if request.method=='POST':
        id=request.form['id']
        result=get_user(id)
        return result   

@app.route('/users', methods=['GET','POST'])
def users():
    if request.method=='GET':
        result=get_all_users()
        return result
    else:
        return jsonify({'error': 'No users found'}), 404
    
@app.route('/login', methods = ['GET','POST'])
def login_app():
    if request.method == 'POST':
        token = request.cookies.get(request.form['email'])
        email=request.form['email']
        password=request.form['password']
        result=verify_token(token,email,password)
        
        if result==1:
            flash('You are Logged')
            return render_template('login.html')

        else:
            data=login(request.form)
            if data['message']=='User logged':
                # Parse the date and time string into a datetime object
                future_time = datetime.strptime(str(data['expires_at']), "%Y-%m-%d %H:%M:%S")
                # Get the current time in seconds
                current_time = datetime.now(tz=timezone.utc).timestamp()
                # Calculate the number of seconds from now
                expires_at = int(future_time.timestamp() - current_time)
                print(expires_at)
                flash('logged','succes')
                resp = make_response(render_template('home.html'))
                resp.set_cookie(request.form['email'],data['token'],expires_at)
                return resp

            elif data==0:
                flash('Email or password invalid')
                return render_template('login.html')
            else:
                flash('Email or password invalid')
            return render_template('login.html')
        

    if request.method == 'GET':
        return render_template('login.html')



if __name__ == '__main__':
    app.run(port=5000)