from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from instance import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    
    # Load the configuration from the instance folder
    app.config.from_object(Config)
    
    # Initialize the database and migrations
    db.init_app(app)
    
    from .models import User, CalorieIntake
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # def create_tables():
    #     db.create_all()
    # Import and register the blueprints
    # from app.routes import bp
    # app.register_blueprint(bp)
    
    return app