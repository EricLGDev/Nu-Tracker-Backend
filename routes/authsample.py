# from flask import Blueprint, render_template, request, flash
# from models import db



# auth = Blueprint('auth', __name__)

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     #log in user
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             if check_password_hash(user.password)
#     return render_template("login.html")

# @auth.route('/logout')
# def logout():
#     return render_template("logout.html")

# @auth.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         firstName = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         if len(email) < 4:
#             flash('Email must be greater than 4 characters.', category='error')
#         elif len(firstName) < 2:
#             flash('Email must be greater than 1 characters.', category='error')
#         elif password1 != password2:
#             flash('passwords dont match!', category='error')
#         elif len(password1) < 7:
#             flash('Email must be greater than 7 characters.', category='error')
#         else: 
#             flash('Account Successfully created!', category='success')
#     return render_template("signup.html")