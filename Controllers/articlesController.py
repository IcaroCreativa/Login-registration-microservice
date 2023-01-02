from flask import request, jsonify
from werkzeug.security import generate_password_hash
import db
from Model import Model
model = Model(db.get_db(), 'articles')

def validate_input(data):
    # Validate the input data
    if not data or not all(key in data for key in ['title', 'body', 'user_id']):
        return False
    return True

def create_article(data):
    # Create a new article
    if not validate_input(data):
        return jsonify({'error': 'Invalid input'}), 400
    model.create(data)
    return jsonify({'message': 'Article created'}), 201

def get_article(id):
    # Retrieve an article from the database
    article = model.read(id)
    if not article:
        return jsonify({'error': 'Article not found'}), 404
    return jsonify({'article': article}), 200

def get_all_articles():
    # Retrieve all articles from the database
    articles = model.read()
    if not articles:
        return jsonify({'error': 'No articles found'}), 404
    return jsonify({'articles': articles}), 200

def update_article(data):
    # Update an existing article
    if  validate_input(data):
        id=data['id']
        # get_all_users from model to verify if article exists
        result=model.read()
        liste=[]
        for i in result:
            # liste.append(str(i[0]))
            if str(i[0])==id :
                id=model.update(data)
                return jsonify({'message': 'Article updated','id':id}), 201  
        return jsonify({'error': 'User doesn\'t exists in DB'}), 404          
        
    else:
        return jsonify({'error': 'Invalid input'}), 400







    # if not validate_input(data):
    #     return jsonify({'error': 'Invalid input'}), 400
    # model.update(data)
    # return jsonify({'message': 'Article updated'}), 200

def delete_article(id):
    # Delete an article from the database
    model.delete(id)
    return jsonify({'message': 'Article deleted'}), 200

