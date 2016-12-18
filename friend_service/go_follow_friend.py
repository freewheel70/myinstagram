from flask import Blueprint
from flask import request
import json
from session import find_session
from pymongo import MongoClient
from utils import email_sender

followfriend = Blueprint('followfriend', __name__, url_prefix='/friend')


@followfriend.route('/follow', methods=['POST'])
def get_all():
    email = request.form['email']
    session_id = request.form['session_id']
    friend_email = request.form['friend_email']
    result = find_session(email)
    loggedin = result['found'] and session_id == result['session_id']
    if not loggedin:
        return json.dumps({'success': False, 'message': 'User not logged in !'})
    else:
        follow(email, friend_email)
        return json.dumps({'success': True, 'username': result['username']})


def follow(myemail, friend_email):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram
    db.users.update_one({'email': myemail}, {'$push': {'friends': friend_email}})
    db.followers.update_one({'email': friend_email}, {'$push': {'followers': myemail}})
    email_sender.send(friend_email, "Hi, you have a new follower !  http://52.221.228.19:8037 ")
