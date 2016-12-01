from celery import Celery
from email_helper import send_weclome_email
from celery.result import AsyncResult


mycelery = Celery('celery_worker',backend='redis://localhost:6379',  broker='amqp://guest@localhost//')


@mycelery.task
def welcome_newuser(email):
    print "receieve message " + email
    send_weclome_email(email)
    return "done"


def get_task_result(task_id):
    result = AsyncResult(task_id)

    if result.successful() or result.failed():
        return "success "
    else:
        return "in progress"

def get_raw_result(task_id):
    return AsyncResult(task_id)