#blueprint is basically roots and url's for the app
from flask import Blueprint, render_template

diary = Blueprint('diary', __name__)

@diary.route('/diary')
def diary_page():
    return render_template("diary.html")