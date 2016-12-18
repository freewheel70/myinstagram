from pymongo import MongoClient


def find_session(email):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    current_session = db.sessions.find_one({'email': email})

    if current_session is None:
        return {"found": False}
    else:
        return {"found": True, 'username': current_session['username'], 'session_id': current_session['session_id']}

