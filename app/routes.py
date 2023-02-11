from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.extensions import db, bcrypt, jwt
from app.models import User

bp = Blueprint("routes", __name__)

@bp.route("/signup", methods=["POST"])
def register():
    # Get the user's information from the request body
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    # Hash the user's password
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    
    # Create a new user
    user = User(username=username, email=email, password=hashed_password)
    
    # Add the user to the database
    db.session.add(user)
    db.session.commit()
    
    # Return a success response
    return jsonify({"message": "User created successfully"}), 201

@bp.route("/login", methods=["POST"])
def login():
    # Get the user's information from the request body
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    # Find the user in the database
    user = User.query.filter_by(username=username).first()
    
    # Check if the user exists and the password is correct
    if user and bcrypt.check_password_hash(user.password, password):
        # Create a JWT token for the user
        access_token = jwt.encode({"username": user.username}, "secret", algorithm="HS256")
        
        # Return the token and a success response
        return jsonify({"access_token": access_token.decode("utf-8")}), 200
    else:
        # Return an error response
        return jsonify({"message": "Invalid username or password"}), 401