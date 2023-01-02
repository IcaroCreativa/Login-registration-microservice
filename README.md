


# Project Name
 Login-registration-microservice

## General Information
This API, written in Python and using the Flask framework, allows you to perform create, read, update, and delete operations on user data stored in a MySQL database.

# Technologies  

List of technologies in this project : 
* <img src="https://www.python.org/static/community_logos/python-logo-inkscape.svg" width="90" alt="Python Logo">[Python](https://www.python.org/) : Version 3.11.1.
* <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" width="30" alt="flask Logo">[Flask](https://flask.palletsprojects.com/en/2.2.x/) : Version 2.2.2
* <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT15d13IJ7gtixCZJXH-N-EctmRjvZyI8yw6BcbTX7A-g&s" width="60" alt="MySQL Logo">[MySQL](https://upload.wikimedia.org/wikipedia/commons/0/0a/MySQL_textlogo.svg) : Version 5.7 +



# Installation  

To use the API, you must have the CRUD user app running on its own server. Before launching the app, please follow the steps below:

After cloning the project, type the following shell commands:   

1. go into the project  
`cd Login-registration-microservice`

2. install flask and flask-mysql with pip  
`pip install flask flask-mysql`

3. Create a MySQL database using a local environment like WAMP or LAMP, and configure the db.py file in config folder to connect to this database using the appropriate connection parameters. Make sure the MySQL server is running before launching the app.
Modify the connector to use your own database
`conn = mysql.connector.connect(user='you username', password='your password', host='localhost', database='your database name')`  

# Launch the app

1. run wamp or lamp server
2. run the app.py file with the command:
 `flask run`
3. To test the API, you can use a software like Postman. In the project, you will find a Postman file (filename.postman_collection.json) containing examples of requests you can send to the API. The API responds with JSON data, except for the GET methods of the login and register routes.
4. You can test the API directly in your browser at [http://127.](http://127.0.0.1:5000/)
5. You can create a user, login, retrieve all users, all articles from home page


## License
This application is open-source under the [MIT license](https://opensource.org/licenses/MIT).  
