from flask import Blueprint
from flask import request
import json
from session import find_session
from pymongo import MongoClient
import pymongo

seefriend = Blueprint('seefriend', __name__, url_prefix='/friend')


@seefriend.route('/see', methods=['POST'])
def see_friend():
    email = request.form['email']
    session_id = request.form['session_id']
    friend_email = request.form['friend_email']
    session_result = find_session(email)
    loggedin = session_result['found'] and session_id == session_result['session_id']
    if not loggedin:
        return json.dumps({'success': False, 'message': 'User not logged in !'})
    else:

        friend_result = fetch_friend(email, friend_email)
        if friend_result["success"]:
            return json.dumps({'success': True,
                               'username': session_result['username'],
                               'friendname': friend_result['friendname'],
                               'images': friend_result["images"],
                               "is_friend": friend_result['is_friend']})
        else:
            return json.dumps({'success': False, 'message': friend_result['message']})


def fetch_friend(email, friend_email):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    friend = db.users.find_one({'email': friend_email})

    if friend is None:
        return {"success": False, "message": "No such user exist"}
    else:
        cursor = db.images.find({'email': friend_email}).sort([("upload_date", pymongo.ASCENDING)])
        images = []
        for image in cursor:
            images.append({"image_path": image["image_path"], "description": image["description"]})

        current_user = db.users.find_one({'email': email})
        is_friend = friend_email in current_user["friends"]

        return {"success": True, "friendname": friend["username"], "images": images, "is_friend": is_friend}
