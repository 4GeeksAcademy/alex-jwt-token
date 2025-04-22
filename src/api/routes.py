"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_bcrypt import Bcrypt  
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import  JWTManager, create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)

jwt = JWTManager()  
bcrypt = Bcrypt()  

# Allow CORS requests to this API
CORS(api)

@api.route('/signup', methods=['POST'])
def create_user():
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
             return jsonify({"msg" : "Email and password are required"}), 400
        
        try:
            user_exists = User.query.filter_by(email=email).first()
            if user_exists:
                return jsonify({"msg" : "User already exists"}), 400
            
            password_encrypted = bcrypt.generate_password_hash(password).decode('utf-8')

            new_user = User(email = email, password = password_encrypted)
            db.session.add(new_user)
            db.session.commit()
           
            return jsonify({"msg" : "user created", "user": new_user.serialize()}), 201 
        
        except Exception as e:
            return jsonify({'error': 'Error in user creation: ' + str(e)}), 500

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
