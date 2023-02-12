from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.extensions import db, bcrypt, jwt
from app.models import User, CalorieIntake
# from app.utils import BLACKLIST

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
        access_token = create_access_token(identity=user.username)

        
        # Return the token and a success response
        return jsonify({"access_token": access_token}), 200
    else:
        # Return an error response
        return jsonify({"message": "Invalid username or password"}), 401

# @bp.route("/logout", methods=["POST"])
# @jwt_required
# def logout():
#     jti = get_jwt_identity()
#     BLACKLIST.add(jti)
#     return jsonify({"message": "Successfully logged out"}), 200

@bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    # Get the current user's identity from the JWT token
    current_user = get_jwt_identity()

    # Find the user in the database
    user = User.query.filter_by(username=current_user).first()

    # Check if the user exists
    if not user:
        return jsonify({"message": "User not found"}), 404

    # Find the user's calorie intake data in the database
    calorie_intakes = CalorieIntake.query.filter_by(user_id=user.id).all()

    # Check if the calorie intake data exists
    if not calorie_intakes:
        return jsonify({"message": "No calorie intake data found for this user"}), 404

    # Create a list of dictionaries to store the calorie intake data
    calorie_intakes_list = []
    for calorie_intake in calorie_intakes:
        calorie_intakes_list.append(calorie_intake.to_dict())

    # Return the calorie intake data and a success response
    return jsonify({"calorie_intakes": calorie_intakes_list}), 200
