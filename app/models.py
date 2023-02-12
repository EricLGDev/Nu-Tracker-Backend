# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .extensions import db


# log_food = db.Table('log_food',
#     db.Column('users_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
#     db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_key=True)
# )

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

class CalorieIntake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    food = db.Column(db.String(50), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Float, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    carbohydrates = db.Column(db.Float, nullable=False)
    sodium = db.Column(db.Float, nullable=False)
    user = db.relationship('User', backref=db.backref('calorie_intakes', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "date": self.date,
            "food": self.food,
            "calories": self.calories,
            "fat": self.fat,
            "protein": self.protein,
            "carbohydrates": self.carbohydrates,
            "sodium": self.sodium
        }

    def __repr__(self):
        return '<CalorieIntake %r>' % self.id

# class Food(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     proteins = db.Column(db.Integer, nullable=False)
#     carbs = db.Column(db.Integer, nullable=False)
#     fats = db.Column(db.Integer, nullable=False)
#     user = db.relationship('User', backref=db.backref('Food', lazy=True))
    

    # @property
    # def calories(self):
    #     return self.proteins * 4 + self.carbs * 4 + self.fats * 9
