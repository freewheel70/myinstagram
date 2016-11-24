from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

db = client.myinstagram

db.users.insert(
    {
        'username': 'freewheel',
        'email': 'freewheel@gamil.com',
        'password': 'hash_value',
        'salt':'random_values',
        'signup_date':datetime.now()
    }
)
