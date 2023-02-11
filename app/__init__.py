from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from instance import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')
    
    # Initialize the database and migrations
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import and register the blueprints
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app