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

@bp.route('/dashboard', methods=['GET'])

@jwt_required()

def get_user_data():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    calorie_intakes = CalorieIntake.query.filter_by(user_id=user.id).all()

    return jsonify([ci.to_dict() for ci in calorie_intakes]), 200

@bp.route("/add", methods=["POST"])
@jwt_required()
def addmacros():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    data = request.get_json()
    food = data.get('food')
    date = data.get('date')
    calories = data.get('calories')
    protein = data.get('protein')
    carbohydrates = data.get('carbohydrates')
    fat = data.get('fat')
    sodium = data.get('sodium')
    if not calories or not protein or not carbohydrates or not fat or not sodium:
        return jsonify({'message': 'invalid data'}), 400

    new_food = CalorieIntake(user_id=user.id,food=food, date=date, calories=calories, protein=protein, carbohydrates=carbohydrates, fat=fat, sodium=sodium)
    
    db.session.add(new_food)
    db.session.commit()
    return jsonify({'message': 'worked'}), 201
    