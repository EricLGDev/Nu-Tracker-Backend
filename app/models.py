from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(130), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class CalorieIntake(db.Model):

    __tablename__ = 'calorie_intake'
    
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    food = db.Column(db.String(80), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('calorie_intakes', lazy=True))

    def __repr__(self):
        return '<CalorieIntake %r>' % self.id