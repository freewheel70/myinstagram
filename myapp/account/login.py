from flask import Blueprint
from flask import request
from flask import render_template
from validator import validate_email
from pymongo import MongoClient
import hashlib
from flask import session


login = Blueprint('login', __name__, url_prefix='/api/login')


@login.route('/newuser', methods=['POST', 'GET'])
def log_in():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            if validate_email(email):
                return find_user(email, password)
            else:
                return "Invalid Input"
        else:
            return "Invalid Method"


def find_user(email, password):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    user = db.users.find_one({'email': email})

    if user is not None:
        password_hash = hashlib.sha256(password.encode() + user['salt'].encode()).hexdigest()
        if password_hash == user['password']:
            session['email'] = email
            return "Login success "+session['email']
        else:
            return "Invalid Password"
    else:
        return "Invalid email"
