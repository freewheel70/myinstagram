from flask import Blueprint
from flask import request
import json
from session import find_session
from pymongo import MongoClient


unfollowfriend = Blueprint('unfollowfriend', __name__, url_prefix='/friend')


@unfollowfriend.route('/unfollow', methods=['POST'])
def unfollow_friend():
    email = request.form['email']
    session_id = request.form['session_id']
    friend_email = request.form['friend_email']
    result = find_session(email)
    loggedin = result['found'] and session_id == result['session_id']
    if not loggedin:
        return json.dumps({'success': False, 'message': 'User not logged in !'})
    else:
        unfollow(email, friend_email)
        return json.dumps({'success': True, 'username': result['username']})


def unfollow(myemail, friend_email):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram
    db.users.update_one({'email': myemail}, {'$pull': {'friends': friend_email}})
    db.followers.update_one({'email': friend_email}, {'$pull': {'followers': myemail}})

