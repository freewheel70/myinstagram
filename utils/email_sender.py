import pika
import json


def send(address, content):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email')

    msg_body = json.dumps({"address": address, "content": content})

    channel.basic_publish(exchange='', routing_key='email', body=msg_body)
    connection.close()


def notify(addresses, content):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notification')

    msg_body = json.dumps({"addresses": addresses, "content": content})
    channel.basic_publish(exchange='', routing_key='notification', body=msg_body)

    connection.close()
