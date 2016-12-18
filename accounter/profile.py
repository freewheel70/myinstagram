from flask import Blueprint
from flask import request
from session import find_session
import json
from pymongo import MongoClient
import pymongo
import redis

profile = Blueprint('profile', __name__, url_prefix='/profile')


@profile.route('/me', methods=['POST'])
def check_login():
    no_cache = request.form['no_cache']
    email = request.form['email']
    session_id = request.form['session_id']
    result = find_session(email)
    loggedin = result['found'] and session_id == result['session_id']
    if loggedin:
        print "no_cache : " + str(no_cache)
        if str(no_cache) == "True":
            # print "Get the updated data"
            images = get_images(email)
            response_json = json.dumps({'loggedin': loggedin,
                                        'username': result['username'],
                                        'images': images})
            save_cache(email, response_json)
        else:
            # print "Get the cached data"
            response_json = get_cache(email, result['username'])

        return response_json
    else:
        return json.dumps({'loggedin': False})


def get_images(email):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    cursor = db.images.find({'email': email}).sort([("upload_date", pymongo.ASCENDING)])
    images = []
    for image in cursor:
        images.append({"image_path": image["image_path"], "description": image["description"]})

    return images


def save_cache(email, response_json):
    redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)
    redis_instance.set(email, response_json)


def get_cache(email, username):
    redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)
    response_json = redis_instance.get(email)
    if response_json is None:
        images = get_images(email)
        response_json = json.dumps({'loggedin': True,
                                    'username': username,
                                    'images': images})
        redis_instance.set(email, response_json)
        # print "Cache Not found : " + email
    # else:
        # print "Cache Hit : " + email

    return response_json
