from pymongo import MongoClient
from datetime import datetime
from flask import Blueprint
from flask import request
from flask import render_template
from validator import validate_email
import hashlib
import uuid

signup = Blueprint('signup', __name__, url_prefix='/api/signup')


@signup.route('/newuser', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            if validate_email(email):
                return save_newuser(email, password)
            else:
                return "Invalid Input"
        else:
            return "Invalid Method"


def save_newuser(email, password):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    user = db.users.find_one({'email': email})

    if user is not None:
        return "The email is already registered"
    else:
        salt = uuid.uuid4().hex
        password_hash = hashlib.sha256(password.encode() + salt.encode()).hexdigest()

        db.users.insert(
            {
                'email': email,
                'password': password_hash,
                'salt': salt,
                'signup_date': datetime.now()
            }
        )

        return "Sign up successfully!"
