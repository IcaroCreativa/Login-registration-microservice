#
Welcome to the API for the CRUD user app! 
This API, written in Python and using the Flask framework, allows you to perform create, read, update, and delete operations on user data stored in a MySQL database.

## Tehcnologies


To use the API, you must have the CRUD user app running on its own server. Before launching the app, please follow the steps below:

Install Flask and the Flask-MySQL connector using pip install flask flask-mysql.
Import Flask and Flask-MySQL into your app.py file with from flask import Flask and from flaskext.mysql import MySQL.
Create a MySQL database using a local environment like WAMP or LAMP, and configure the app.py file to connect to this database using the appropriate connection parameters. Make sure the MySQL server is running before launching the app.
To test the API, you can use a software like Postman. In the project, you will find a Postman file (filename.postman_collection.json) containing examples of requests you can send to the API. The API responds with JSON data, except for the GET methods of the login and register routes.

In addition to the CRUD user app, you can also run a separate client app (client.py) on its own server. This app, written in Python and using the Flask framework, will not have its own database, but will instead render the JSON data from the CRUD user app. This client file allows you to test the API by opening a connection on a different port.

Thank you for using this API!


# Project Name
 Login-registration-microservice



## General Information
This API, written in Python and using the Flask framework, allows you to perform create, read, update, and delete operations on user data stored in a MySQL database.

# Technologies  



Liste des technologies utilisées dans ce projet : 
* <img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="90" alt="Laravel Logo">[Laravel Breeze](https://laravel.com/docs/9.x/starter-kits) : Version 9.
* <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" width="30" alt="flask Logo">[Flask](https://vue3-fr.netlify.app/guide/migration/introduction.html) : Version 2.2.2
* <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT15d13IJ7gtixCZJXH-N-EctmRjvZyI8yw6BcbTX7A-g&s" width="60" alt="MySQL Logo">[MySQL](https://upload.wikimedia.org/wikipedia/commons/0/0a/MySQL_textlogo.svg) : Version 5.7 +



# Installation  

To use the API, you must have the CRUD user app running on its own server. Before launching the app, please follow the steps below:

After cloning the project, type the following shell commands:   

1. go into the project  
`cd Login-registration-microservice`

2. install flask and flask-mysql with pip  
`pip install flask flask-mysql`

3. Create a MySQL database using a local environment like WAMP or LAMP, and configure the app.py file to connect to this database using the appropriate connection parameters. Make sure the MySQL server is running before launching the app.  

# Create a instance of MySQL to connect with python on databse
`mysql = MySQL(autocommit=True)
app.config['MYSQL_DATABASE_USER'] = 'your username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your password'
app.config['MYSQL_DATABASE_DB'] = 'your databse name'
app.config['MYSQL_DATABASE_HOST'] = ' your database host'
app.config['MYSQL_DATABASE_PORT'] = port of your host`

4. install npm dependencies  
`npm install`

5. generate a key for your application  
`php artisan key:generate`

6. add the database connection config to your .env file  
`DB_CONNECTION=mysql`  
`DB_HOST=127.0.0.1`  
`DB_PORT=3306`  
`DB_DATABASE=commit_yowl`  
`DB_USERNAME=root`  
`DB_PASSWORD=*votre mot de passe de mysql*`

7. run the migration files to generate the schema  
`php artisan migrate`

8. seed your database with some users, categories, posts and comments  
`php artisan db:seed`

9. run webpack in 2 terminals  
`npm run dev`
`php artisan serve`  

10. Warning !  
Requires prior installation of Nodejs   
[nodejs](https://nodejs.org/en/)  


## License
This application is open-source under the [MIT license](https://opensource.org/licenses/MIT).  
