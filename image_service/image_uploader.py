from flask import Blueprint
from flask import request
import os
import time
import random
import json
from session import find_session
from pymongo import MongoClient
from datetime import datetime
from utils import keyword_sender
from utils import email_sender
import hashlib

upload = Blueprint('upload', __name__, url_prefix='/image')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = "./myapp/static/images"
RESIZED_FOLDER = "./myapp/static/resized"
THUMBNAIL_FOLDER = "./myapp/static/thumbnails"


def secure_filename():
    filename = time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + '-' + str(random.randint(10000, 99999))
    return filename


@upload.route('/newimage', methods=['POST'])
def upload_img():
    global UPLOAD_FOLDER

    email = request.form['email']
    session_id = request.form['session_id']

    result = find_session(email)
    loggedin = result['found'] and session_id == result['session_id']
    if not loggedin:
        return json.dumps({'success': False, 'message': 'User not logged in !'})

    try:
        file = request.files['image']
        rawfilename = request.form['filename']
        description = request.form["description"]
        extension = rawfilename.rsplit('.', 1)[1]
        filename = secure_filename()

        hash_md5 = hashlib.md5(email)
        directory_path = hash_md5.hexdigest()

        final_file_name = os.path.join(UPLOAD_FOLDER+"/"+directory_path, filename + "." + extension)
        assure_path_exists(final_file_name)
        file.save(final_file_name)

        image_path = '/images/' + directory_path + "/" + filename + "." + extension
        save_image_info(email, image_path, description)
        keyword_sender.send_keywork_job(email, image_path, description)
        notify_followers(email, result['username'])
        return json.dumps({'success': True, 'path': image_path})
    except IOError as e:
        return json.dumps({'success': False, 'message': 'Error 1 : Fail to save image -- ' + rawfilename})
    except IndexError as e1:
        return json.dumps({'success': False, 'message': 'Error 2 : Fail to save image filename -- ' + rawfilename})


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def save_image_info(email, image_path, description):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    db.images.insert(
        {
            'email': email,
            'image_path': image_path,
            'upload_date': datetime.utcnow(),
            'description': description
        }
    )


def notify_followers(email, username):
    content = username + " just upload a new photo ! Go to take a look ! http://52.221.228.19:8037 "
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram
    result = db.followers.find_one({'email': email})
    followers = result['followers']
    email_sender.notify(followers, content)
