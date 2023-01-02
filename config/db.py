import mysql.connector

def get_db():
    # Connect to the MySQL database and return the connection object
    # Modify the connector to use your own database
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='schema')
    return conn


def init_db():
    # Initialize the MySQL database with the necessary tables
    conn = get_db()
    cursor = conn.cursor()

    # Create the articles table
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT,
                        title VARCHAR(255) NOT NULL,
                        body TEXT NOT NULL,
                        creation_date DATETIME NOT NULL,
                        modified_at DATETIME NOT NULL,
                        user_id INTEGER NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users(id)
                    )''')

    # Create the users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL UNIQUE,
                        password VARCHAR(255) NOT NULL,
                        modified_at DATETIME NOT NULL
                    )''')

    # # Create the users token
    # cursor.execute('''CREATE TABLE IF NOT EXISTS tokens (
    #                     id INTEGER PRIMARY KEY AUTO_INCREMENT,
    #                     user_id INTEGER NOT NULL,
    #                     token VARCHAR(255) NOT NULL UNIQUE,
    #                     created_at DATETIME NOT NULL,
    #                     expires_at DATETIME NOT NULL
                        
    #                 )''')

    conn.commit()
    cursor.close()
    conn.close()


# init_db()
