from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.myinstagram

db.users.delete_many({})
db.sessions.delete_many({})
db.images.delete_many({})
db.keywords.delete_many({})
db.followers.delete_many({})