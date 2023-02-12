from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sqlalchemy.sql import text


import os

db = SQLAlchemy()

# Initialize App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SECRET_KEY'] = 'ForbiddenKey'
app.config.from_pyfile('config/config.cfg')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initialize Database
db.init_app(app)
migrate = Migrate(app, db)



# Initialize Marshmallow
ma = Marshmallow

#importing pathways
from routes.views import views
from routes.macros import macros
from routes.diary import diary
from routes.auth import auth


#import databases


#url prefix is how you access the blueprint
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(macros, url_prefix='/')
app.register_blueprint(diary, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

#creating database


# this route will test the database connection and nothing more

if __name__ == '__main__':
    app.run(debug=True)

# Test Route for Postman; delete later
#@app.route('/', methods=['GET'])
#def get():
    #return jsonify({ 'msg': 'Test success'})