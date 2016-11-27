from celery import Celery

from myapp.utils.email_helper import send_weclome_email

mycelery = Celery('celery_worker', backend='redis://localhost:6379', broker='amqp://guest@localhost//')

@mycelery.task
def welcome_newuser(email):
    send_weclome_email(email)
    return "done"