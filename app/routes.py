from flask import Blueprint, request, jsonify, session, redirect, url_for, flash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.extensions import db, bcrypt, jwt
from app.models import User, CalorieIntake

# from app.utils import BLACKLIST

bp = Blueprint("routes", __name__)

@bp.route("/")
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return 'Logged in as %s' % session['username']


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
    print("Username: ", username)
    print("Password: ", password)

    # Find the user in the database
    user = User.query.filter_by(username=username).first()

    print("User: ", user)

    # Check if the user exists and the password is correct
    if user:
        if bcrypt.check_password_hash(user.password, password):
            # Create a JWT token for the user
            access_token = create_access_token(identity=user.id)
            print("Access token: ", access_token)

            # Return the token and a success response
            return jsonify({
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 200
    else:
        # Return an error response
        return jsonify({"message": "Invalid username or password"}), 401


@bp.route('/diary/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_data(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return jsonify({"message": "User not found"}), 404
    
    calorie_intakes = CalorieIntake.query.filter_by(user_id=user.id).all()

    return jsonify([ci.to_dict() for ci in calorie_intakes]), 200


@bp.route("/diary", methods=["POST"])
@jwt_required()
def addmacros():
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first()
    data = request.get_json()
    food = data.get('food')
    date = data.get('date')
    calories = data.get('calories')
    protein = data.get('protein')
    carbohydrates = data.get('carbohydrates')
    fat = data.get('fat')
    if not calories or not protein or not carbohydrates or not fat:
        return jsonify({'message': 'invalid data'}), 400

    new_food = CalorieIntake(user_id=user.id,food=food, date=date, calories=calories, protein=protein, carbohydrates=carbohydrates, fat=fat)
    
    db.session.add(new_food)
    db.session.commit()
    return jsonify({'message': 'Entry added'}), 201
    
@bp.route('/diary/<int:id>', methods=['PUT'])
@jwt_required()
def update_entry(id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first()
    if not user:
        return jsonify({"message": "Invalid user"}), 401

    entry = CalorieIntake.query.filter_by(id=id).first()
    if not entry:
        return jsonify({"message": "Invalid entry"}), 404

    if entry.user_id != user.id:
        return jsonify({"message": "Unauthorized access"}), 401

    data = request.get_json()
    entry.calories = data.get('calories')
    entry.date = data.get('date')

    try:
        db.session.commit()
        return jsonify({"message": "Entry updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

@bp.route('/diary/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_calorie_intake(id):
    user_id = get_jwt_identity()
    print(user_id)

    calorie_intake = CalorieIntake.query.get(id)

    if calorie_intake is None:
        return jsonify({"error": "Calorie intake data with id {} does not exist".format(id)}), 404

    if calorie_intake.user_id != user_id:
        return jsonify({"error": "You do not have permission to delete this data"}), 403

    db.session.delete(calorie_intake)
    db.session.commit()

    return jsonify({"message": "Calorie intake data with id {} has been deleted".format(id)}), 200
