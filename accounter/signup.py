import hashlib
import uuid
from datetime import datetime
import json
from flask import Blueprint
from flask import request
from pymongo import MongoClient

from utils import email_sender
from validator import validate_email

signup = Blueprint('signup', __name__, url_prefix='/signup')


@signup.route('/newuser', methods=['POST'])
def sign_up():
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    if validate_email(email):
        return save_newuser(username, email, password)
    else:
        return json.dumps({"success": False, "message": "Invalid email pattern"})


def save_newuser(username, email, password):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    user = db.users.find_one({'email': email})

    if user is not None:
        return json.dumps({"success": False, "message": "The email is already registered"})
    else:
        salt = uuid.uuid4().hex
        password_hash = hashlib.sha256(password.encode() + salt.encode()).hexdigest()

        db.users.insert(
            {
                'username': username,
                'email': email,
                'password': password_hash,
                'salt': salt,
                'signup_date': datetime.now(),
                'friends': []
            }
        )

        db.followers.insert(
            {
                'email': email,
                'followers': []
            }
        )

        email_sender.send(email, "Welcome To Freewheel Photos !  http://52.221.228.19:8037 ")
        return json.dumps({"success": True})
