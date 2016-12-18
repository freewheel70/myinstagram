from flask import Blueprint
from flask import request
import json
from session import find_session
from pymongo import MongoClient

myfriends = Blueprint('myfriends', __name__, url_prefix='/friend')


@myfriends.route('/mine', methods=['POST'])
def get_all():
    email = request.form['email']
    session_id = request.form['session_id']
    result = find_session(email)
    loggedin = result['found'] and session_id == result['session_id']
    if not loggedin:
        return json.dumps({'success': False, 'message': 'User not logged in !'})
    else:
        all_users = fetch_my_friends(email)
        return json.dumps({'success': True, 'username': result['username'], 'friends': all_users})


def fetch_my_friends(email):
    result = []
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram
    current_user = db.users.find_one({'email': email})
    my_friends = current_user['friends']

    all_users = db.users.find({'email': {'$ne': email}})
    for user in all_users:
        friend_email = user["email"]
        if friend_email in my_friends:
            result_obj = {"username": user['username'],
                          "email": friend_email,
                          "link": "http://52.221.228.19:8037/api/friend/see?friend_email=" + friend_email,
                          "followed": 1}
            result.append(result_obj)

    return result
