from pymongo import MongoClient
import hashlib
import uuid


def find_session(email):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    current_session = db.sessions.find_one({'email': email})

    if current_session is None:
        return {"found": False}
    else:
        return {"found": True, 'username': current_session['username'], 'session_id': current_session['session_id']}


def new_session(username, email):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    salt = uuid.uuid4().hex
    session_id = hashlib.sha256(salt.encode()).hexdigest()

    db.sessions.insert(
        {
            'email': email,
            'username': username,
            'session_id': session_id
        }
    )

    return session_id


def remove_session(email):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram
    db.sessions.delete_many({'email': email})
