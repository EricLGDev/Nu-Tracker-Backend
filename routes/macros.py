#blueprint is basically roots and url's for the app
from flask import Blueprint, render_template, request, flash
from models import AddCalories, CalorieIntakeModel
from app import db



macros = Blueprint('macros', __name__)

@macros.route('/macros', methods=['GET', 'POST'])
def addMacros_page():
    form1 = AddCalories()
    if form1.validate_on_submit():
        name = request.form['name']
        calories = request.form['calories']
        protein = request.form['protein']
        carbs = request.form['carbs']
        fat = request.form['fat']
        #updated = stringdate()
        record = CalorieIntakeModel(name, calories, protein, carbs, fat)
        db.session.add(record)
        db.session.commit()
        message = f"the data for food {name} has been updated"
        return render_template('macros.html', message=message)
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('macros.html', form1=form1)
