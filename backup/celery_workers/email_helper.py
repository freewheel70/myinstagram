import sendgrid
from sendgrid.helpers.mail import *

from asyncworker.keys import sendGridKey


def send_weclome_email(address):
    subject = "Weclome to MyInstagram"
    content = "Welcome to MyInstagram!\nLearn more in http://52.221.228.19:8037"
    send_email(address, subject, content)


def send_email(address, subject, contents):
    apikey = sendGridKey()
    sg = sendgrid.SendGridAPIClient(apikey=apikey)
    from_email = Email("notification@myinstagram.com")
    to_email = Email(address)
    subject = subject
    content = Content("text/plain", contents)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)
