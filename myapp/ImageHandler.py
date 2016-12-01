import base64
import json
import os
import random
import time
from os import listdir

import CurrentPort
import MyResponse
from PIL import Image
from celery import Celery
from celery.result import AsyncResult
from flask import request

from backup.celery_workers import email_helper

mycelery = Celery('ImageHandler', backend='redis://localhost:6379', broker='amqp://guest@localhost//')

UPLOAD_FOLDER = "./static/images"
RESIZED_FOLDER = "./static/resized"
THUMBNAIL_FOLDER = "./static/thumbnails"


def decode_image(imgstring, save_path):
    imgdata = base64.b64decode(imgstring)
    with open(save_path, 'wb') as f:
        f.write(imgdata)


def datetime_filename():
    filename = time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + '-' + str(random.randint(10000, 99999))
    return filename


def get_image_url(filename):
    return str(request.url).replace(":" + str(CurrentPort.get_current_portnumber()) + "/app/submit_image",
                                    "/images/") + filename


def get_thumbnail_url(thumbnail_filename):
    return str(request.url).replace(":" + str(CurrentPort.get_current_portnumber()) + "/app/submit_image",
                                    "/thumbnails/") + thumbnail_filename


def get_reized_image_url(resized_filename, url, port):
    return url.replace(":" + port + "/app/resize_image",
                       "/resized/") + resized_filename


def get_resized_thumbnail_url(thumbnail_filename, url, port):
    return url.replace(":" + port + "/app/resize_image",
                       "/thumbnails/") + thumbnail_filename


def get_extension():
    return "jpg"


def create_thumbnail(image_path, unique_datetime_label, extension):
    global THUMBNAIL_FOLDER

    fd = open(image_path, "rb")
    im = Image.open(fd)
    if im.width < im.height:
        size = 64, im.height * 64 / im.width
        im = im.resize(size)
        region = 0, im.height / 2 - 32, 64, im.height / 2 + 32
        im = im.crop(region)
    elif im.height < im.width:
        size = im.width * 64 / im.height, 64
        im = im.resize(size)
        region = im.width / 2 - 32, 0, im.width / 2 + 32, im.height
        im = im.crop(region)
    else:
        size = 64, 64
        im = im.resize(size)

    thumbnail_name = unique_datetime_label + ".tn" + "." + extension
    im.save(os.path.join(THUMBNAIL_FOLDER, thumbnail_name))
    return thumbnail_name


def create_resized_image(image_path, unique_datetime_label, extension, dimension):
    global RESIZED_FOLDER

    fd = open(image_path, "rb")
    im = Image.open(fd)
    if dimension > 0:
        if im.width > im.height:
            size = dimension, im.height * dimension / im.width
            im = im.resize(size)
        elif im.height > im.width:
            size = im.width * dimension / im.height, dimension
            im = im.resize(size)
        else:
            size = dimension, dimension
            im = im.resize(size)

    resized_name = unique_datetime_label + ".re" + "." + extension
    im.save(os.path.join(RESIZED_FOLDER, resized_name))
    return resized_name


def get_recent_records(current_image):
    global UPLOAD_FOLDER
    records = []
    counter = 0
    files = listdir(UPLOAD_FOLDER)
    files = [os.path.join(UPLOAD_FOLDER, f) for f in files]
    files.sort(key=lambda x: -os.path.getmtime(x))
    files = [os.path.basename(f) for f in files]
    for filename in files:
        if filename == current_image:
            continue
        temp_file_list = str(filename).rsplit('.')
        thumbnail_name = temp_file_list[0] + ".tn." + temp_file_list[1]
        records.append(MyResponse.ImageNamesTuple(get_image_url(filename), get_thumbnail_url(thumbnail_name)))
        counter += 1
        if counter == 3:
            break
    return records


def post_image_result():
    if 'image' not in request.form:
        print "No image found in request.form"
        result = MyResponse.FailureResponse("fail", CurrentPort.get_current_portnumber(), "No image found!")
    else:
        image_str = str(request.form['image']).strip()
        if image_str == '':
            print "image string is empty"
            result = MyResponse.FailureResponse("fail", CurrentPort.get_current_portnumber(), "No image found!")
        else:
            global UPLOAD_FOLDER
            extension = get_extension()
            unique_datetime_label = datetime_filename()
            server_filename = unique_datetime_label + "." + extension
            file_path = os.path.join(UPLOAD_FOLDER, server_filename)
            print "image save file path : " + file_path
            decode_image(image_str, file_path)

            thumbnail_filename = create_thumbnail(file_path, unique_datetime_label, extension)

            result = MyResponse.NormalImageResponse("success", CurrentPort.get_current_portnumber(),
                                                    get_image_url(server_filename),
                                                    get_thumbnail_url(thumbnail_filename),
                                                    get_recent_records(server_filename))

    return result.to_json()


@mycelery.task
def process_resize_image(image_str, dimension, email, url, port, test_delay=False):
    global UPLOAD_FOLDER
    if test_delay:
        print "process_resize_image sleep for 30 secs"
        time.sleep(30)
    extension = get_extension()
    unique_datetime_label = datetime_filename()
    server_filename = unique_datetime_label + "." + extension
    file_path = os.path.join(UPLOAD_FOLDER, server_filename)
    print "image save file path : " + file_path
    decode_image(image_str, file_path)

    resized_filename = create_resized_image(file_path, unique_datetime_label, extension,
                                            dimension)
    thumbnail_filename = create_thumbnail(file_path, unique_datetime_label, extension)

    email_content = "resized image url:" + get_reized_image_url(
        resized_filename, url, port) + "\n thumbnail url: " + get_resized_thumbnail_url(
        thumbnail_filename, url, port)

    email_helper.send_email(email, email_content)
    return "done"


def resize_image_result():
    if 'image' not in request.form:
        print "No image found in request.form"
        return MyResponse.FailureResponse("fail", CurrentPort.get_current_portnumber(), "No image found!").to_json()
    if 'email' not in request.form or request.form['email'].strip() == '':
        print "No email found in request.form"
        return MyResponse.FailureResponse("fail", CurrentPort.get_current_portnumber(), "No email found!").to_json()
    if 'dimension' not in request.form or request.form['dimension'].strip() == '':
        print "No dimension found in request.form"
        return MyResponse.FailureResponse("fail", CurrentPort.get_current_portnumber(), "No dimension found!").to_json()

    image_str = str(request.form['image']).strip()
    if image_str == '':
        print "image string is empty"
        return MyResponse.FailureResponse("fail", CurrentPort.get_current_portnumber(), "No image found!").to_json()
    else:
        if 'delay' in request.form and request.form['delay'] == '1':
            test_delay = True
        else:
            test_delay = False

        new_task = process_resize_image.delay(image_str,
                                              int(request.form['dimension']),
                                              str(request.form['email']).strip(),
                                              str(request.url),
                                              str(CurrentPort.get_current_portnumber()),
                                              test_delay)
        task_id = new_task.task_id
        result = {"status": "success", "task_id": task_id}
        return json.dumps(result)


def get_task_result():
    if "task_id" not in request.form or request.form['task_id'].strip() == '':
        return MyResponse.FailureResponse("fail", CurrentPort.get_current_portnumber(), "No task_id found!").to_json()
    else:
        result = AsyncResult(request.form['task_id'])

        response = {"status": "success", "resize_status": "finished"}
        if result.successful() or result.failed():
            return json.dumps(response)
        else:
            response = {"status": "success", "resize_status": "in progress"}
            return json.dumps(response)
