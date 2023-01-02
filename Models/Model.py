import mysql.connector
from flask import request, jsonify



class Model:
    def __init__(self, db_connection, table):
        self.conn = db_connection
        self.table = table

    def create(self, data):
        # Insert a new record into the MySQL database using the MySQL connector
        cursor = self.conn.cursor()
        if self.table=='articles':
            query = 'INSERT INTO `articles` (`id`, `title`, `body`, `creation_date`,`modified_at`, `user_id`) VALUES (NULL, %(title)s, %(body)s, NOW(),NOW(), %(user_id)s)'
            cursor.execute(query, data)
        elif self.table=='users':
            query = 'INSERT INTO `users` (`id`, `username`, `email`, `password`, `created_at`, `modified_at`) VALUES (NULL, %(username)s, %(email)s, %(password)s, NOW(), NOW())'
            cursor.execute(query, data)
        elif self.table=='tokens':
            query = 'INSERT INTO `tokens` (`id`, `user_id`, `token`, `created_at`, `expires_at`) VALUES (NULL, %(user_id)s, %(token)s, NOW(), %(expires_at)s)'
            cursor.execute(query, data)

        self.conn.commit()
        id = cursor.lastrowid
        cursor.close()
        return id

    def read(self, id=None):
        # Retrieve one or all records from the MySQL database using the MySQL connector
        cursor = self.conn.cursor()
        if id:
            cursor.execute(f'SELECT * FROM {self.table} WHERE id = %s', (id,))
            result = cursor.fetchone()
        else:
            cursor.execute(f'SELECT * FROM {self.table}')
            result = cursor.fetchall()
        cursor.close()
        return result
        
    def update(self, data):
        # Update an existing record in the MySQL database using the MySQL connector
        cursor = self.conn.cursor()
        if self.table=='users':
            query = 'UPDATE `users` SET `username` = %(username)s, `email` = %(email)s, `password` = %(password)s,`modified_at` = NOW() WHERE `id` = %(id)s' 
            cursor.execute(query, data)
        elif self.table=='articles':
            query = 'UPDATE `articles` SET `title` = %(title)s, `body` = %(body)s, `modified_at` = NOW(),`user_id` = %(user_id)s WHERE `id` = %(id)s'
            cursor.execute(query, data)
        self.conn.commit()
        cursor.close()        
        id=data['id']
        return id

    def delete(self, id):
        # Delete a record from the MySQL database using the MySQL connector
        cursor = self.conn.cursor()
        if self.table=='users':
            cursor.execute(f'DELETE FROM {self.table} WHERE id = %s', (id,))
            cursor.execute(f'DELETE FROM `articles` WHERE user_id = %s', (id,))
        else:
            cursor.execute(f'DELETE FROM {self.table} WHERE id = %s', (id,))
        self.conn.commit()
        cursor.close()
        