from app import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from datetime import date




class UserModel(db.Model, UserMixin):

    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    #calorieNotes = db.relationship('CalorieIntakeModel')
    #calorieMacros = db.relationship('MacroModel')

    def __repr__(self):
        return '<User %r>' % self.username

class CalorieIntakeModel(db.Model):

    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    updated = db.Column(db.String)
    #userModel_id = db.Column(db.Integer. db.ForeignKey('UserModel.id'))

    def __init__(self, name, date, calories, protein, carbs, fat, updated):
        self.name = name
        self.date = date
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.updated = updated
        #return '<CalorieIntake %r>' % self.id

class AddCalories(FlaskForm):
    id_field = HiddenField()
    name = StringField('Food name')
    date = StringField('MM/DD/YYYY')
    calories = IntegerField('Calorie amount')
    protein = IntegerField('protein amount')
    carbs = IntegerField('carbs amount')
    fat = IntegerField('fat amount')
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')

class MacroModel(db.Model):

    __tablename__ = 'macro_tabel'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    carbohydrates = db.Column(db.Float, nullable=False)
    fat = db.Column(db.Float, nullable=False)
    #userModel_id = db.Column(db.Interger. db.ForeignKey('UserModel.id'))

    def __repr__(self):
        return '<Macro %r>' % self.id


