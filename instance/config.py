from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'DATABASE_URI'
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False