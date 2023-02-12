from flask import Flask
from flask_migrate import Migrate
from instance import Config
from . import models, routes
from .extensions import db, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    
    # Load the configuration from the instance folder
    app.config.from_object(Config)
    
    # Initialize the database and migrations
    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    with app.app_context():
        db.create_all()
    # Import and register the blueprints
    app.register_blueprint(routes.bp)
    
    return app