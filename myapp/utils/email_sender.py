import pika
import json


def send(address, content):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email')

    msg_body = json.dumps({"address": address, "content": content})

    channel.basic_publish(exchange='', routing_key='email', body=msg_body)
    print(" [x] Sent " + msg_body)
    connection.close()
