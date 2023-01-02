from flask import request, jsonify
import hashlib
import db
from Model import Model
from pprint import pprint
from werkzeug.datastructures import ImmutableMultiDict
import uuid
from datetime import datetime, timedelta

model = Model(db.get_db(), 'users')

def validate_input(data):
    # Validate the input data
    if not data or not all(key in data for key in ['username', 'email', 'password']):
        return False
    return True

def create_user(data):

    if  validate_input(data):
       #Create a new user
        email=data['email']
        password=data['password']
        hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        data = ImmutableMultiDict([('username', data['username']), ('email', data['email']), ('password', hash)])
        
        result=model.read()
        for i in result:
            print(len(result))
            if i[2]!=email:
                id=model.create(data)
                return jsonify({'message': 'User created','id':id}), 201  
            else:
                return jsonify({'error': 'Email exists in DB'}), 404 
    
    else:
        return jsonify({'error': 'Invalid input'}), 400

        

    
 

def get_user(id):
    # Retrieve an user from the database
    user = model.read(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'user': user}), 200

def get_all_users():
    # Retrieve all users from the database
    users = model.read()
    if not users:
        return jsonify({'error': 'No users found'}), 404
    return jsonify({'users': users}), 200

def update_user(data):
    # Update an existing user
    if  validate_input(data):
        #Create a new user
        id=data['id']
        email=data['email']
        password=data['password']
        hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        data = ImmutableMultiDict([('id', data['id']), ('username', data['username']), ('email', data['email']), ('password', hash)])
        # get_all_users from model to verify if email exists
        result=model.read()
        for i in result:
            if str(i[0])==id and i[2]==email:
                id=model.update(data)
                return jsonify({'message': 'User updated','id':id}), 201  
        return jsonify({'error': 'User doesn\'t exists in DB'}), 404          
        
    else:
        return jsonify({'error': 'Invalid input'}), 400


def delete_user(id):
    # Delete an user from the database
    model.delete(id)
    return jsonify({'message': 'User deleted'}), 200


def login(data):
    # Update an existing user
    
    #Search the user in database
    id=''
    email=data['email']
    password=data['password']
    
    hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # generate a Universally unique Identifier
    token=str(uuid.uuid4())
    # Get the current date and time
    now = datetime.now()
    # Calculate the date and time one month in the future
    expires_at = str(now + timedelta(days=30))
    
    
    # get_all_users from model to verify if email exists
    result=model.read()
    
    for i in result:
        
        if str(i[2])==email and str(i[3])==hash:
            id=str(i[0]) #Recupere l'id si l'email existe
            data = ImmutableMultiDict([('user_id', id), ('token', token), ('expires_at', expires_at)])
            model_token = Model(db.get_db(), 'tokens')
            id=model_token.create(data)
            token=model_token.read(id)
            # return jsonify({'message': 'User logged','token':token[2]}), 201
            # print(token[0])
            # print(token[1])
            # print(token[2])
            # print(token[3])
            # print(token[4])
            return {'message': 'User logged','token':token[2],'expires_at':token[4]}
        
    return jsonify({'error': 'User doesn\'t exists in DB'}), 404
              
def verify_token(token,email,password):
    if token!=None:
        model_token = Model(db.get_db(), 'tokens')
        tokens=model_token.read()
        users=model.read()
        user_id=0
        hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user_password=''
        for user in users:
            if str(user[2])==email:
                user_id=str(user[0])
                user_password=str(user[3])
        # print('Id is: ')
        # print(user_id)
        # print('------------')
        for i in tokens:
            # print(i[2])
            # print(i[1])
            # print(i[4])
            if token ==str(i[2]) and str(i[1])==user_id and hash==user_password:
                # Parse the date string into a datetime object
                expires_at = datetime.strptime(str(i[4]), "%Y-%m-%d %H:%M:%S")
                # Current date
                now = datetime.now()
                # Compare the dates
                if expires_at >= now:
                    return 1 # the token ok
                else:
                    return 0  # the token has expired

        return 0    
    
    else:
        return -1  # No token was done!       
        
    


