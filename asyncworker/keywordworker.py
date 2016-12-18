import pika
import json
import re
from pymongo import MongoClient

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='keyword')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    message = json.loads(body)
    email = message['email']
    image_path = message['image_path']
    description = message['description']
    process_keyword(email, image_path, description)


def process_keyword(email, image_path, description):
    client = MongoClient("mongodb://localhost:27017")
    db = client.myinstagram

    words = re.split('[^a-z0-9]+', description.lower())
    uniqueWords = set(words)

    for word in uniqueWords:
        db.keywords.insert(
            {
                'email': email,
                'image_path': image_path,
                'keyword': word,
                'description':description
            })


channel.basic_consume(callback, queue='keyword', no_ack=True)
channel.start_consuming()
