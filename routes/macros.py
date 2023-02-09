#blueprint is basically roots and url's for the app
from flask import Blueprint, render_template

macros = Blueprint('macros', __name__)

@macros.route('/macros')
def macros_page():
    return render_template("macros.html")