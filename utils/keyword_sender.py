import pika
import json


def send_keywork_job(email, image_path, description):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='keyword')

    msg_body = json.dumps({"email": email, "image_path": image_path, "description": description})

    channel.basic_publish(exchange='', routing_key='keyword', body=msg_body)
    connection.close()
