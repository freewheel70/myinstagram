from flask import Blueprint
from flask import request
import json
from session import find_session
import re
from pymongo import MongoClient

search = Blueprint('search', __name__, url_prefix='/image')


@search.route('/search', methods=['POST'])
def search_img():
    keyword = request.form['keyword']
    email = request.form['email']
    session_id = request.form['session_id']
    words = re.split('[^a-z0-9]+', keyword.lower())
    if len(words) == 0:
        return json.dumps({'success': False, 'message': 'No valid keyword found !'})
    else:
        keyword = words[0]
    result = find_session(email)
    loggedin = result['found'] and session_id == result['session_id']
    if not loggedin:
        return json.dumps({'success': False, 'message': 'User not logged in !'})
    else:
        images = search_keyword(email, keyword)
        return json.dumps({'success': True, 'username': result['username'], 'images': images})


def search_keyword(email, keyword):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram
    cursor = db.keywords.find({'email': email, 'keyword': keyword})
    images = []
    for image in cursor:
        images.append({"image_path": image["image_path"], "description": image["description"]})
    return images
