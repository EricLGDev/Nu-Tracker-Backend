from flask import request, jsonify, make_response
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash