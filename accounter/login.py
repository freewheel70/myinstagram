from flask import Blueprint
from flask import request
from validator import validate_email
from pymongo import MongoClient
import hashlib
from session import new_session, remove_session
import json

login = Blueprint('login', __name__, url_prefix='/login')


@login.route('/newuser', methods=['POST'])
def log_in():
    if request.method == 'POST':
        email = request.form['email']
        # check whether has logged in
        # current_session = find_session(email)
        # if current_session['found']:
        #     return json.dumps({"success": True,
        #                        "profile_url": "http://52.221.228.19:8037/api/profile/me?email=" + email + "&id=" +
        #                                       current_session['session_id']})
        password = request.form['password']
        if validate_email(email):
            return find_user(email, password)
        else:
            return json.dumps({"success": False, "message": "Invalid Input"})
    else:
        return json.dumps({"success": False, "message": "Invalid Method"})


def find_user(email, password):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    user = db.users.find_one({'email': email})

    if user is not None:
        password_hash = hashlib.sha256(password.encode() + user['salt'].encode()).hexdigest()
        if password_hash == user['password']:
            remove_session(email)
            session_id = new_session(user['username'], email)
            return json.dumps({"success": True,
                               "session_id": session_id})
        else:
            return json.dumps({"success": False, "message": "Invalid email or password"})
    else:
        return json.dumps({"success": False, "message": "Invalid email or password"})
