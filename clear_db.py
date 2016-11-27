from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.myinstagram

db.users.delete_many({})