from flask import Blueprint
from flask import request
import json
from session import find_session
import os
from pymongo import MongoClient

remove = Blueprint('remove', __name__, url_prefix='/image')


@remove.route('/remove', methods=['POST'])
def remove_img():
    image = request.form['image']
    email = request.form['email']
    session_id = request.form['session_id']

    result = find_session(email)
    loggedin = result['found'] and session_id == result['session_id']
    if not loggedin:
        return json.dumps({'success': False, 'message': 'User not logged in !'})
    else:
        remove_from_dbfs(image)
        return json.dumps({'success': True})


def remove_from_dbfs(image):
    os.remove("/home/ubuntu/myproject/myapp/static" + image)

    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram
    db.images.delete_many({'image_path': image})
