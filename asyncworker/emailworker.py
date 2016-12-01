import pika
import json
import sendgrid
from sendgrid.helpers.mail import *
from keys import sendGridKey

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='email')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    email = json.loads(body)
    send_email(email['address'], "MyInstagram Notification", email['content'])


def send_email(address, subject, contents):
    apikey = sendGridKey()
    sg = sendgrid.SendGridAPIClient(apikey=apikey)
    from_email = Email("notification@myinstagram.com")
    to_email = Email(address)
    subject = subject
    content = Content("text/plain", contents)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())


channel.basic_consume(callback, queue='email', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
