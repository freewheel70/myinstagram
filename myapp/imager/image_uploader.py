from flask import Blueprint
from flask import request
from flask import render_template
import requests
import json

upload = Blueprint('upload', __name__, url_prefix='/api/upload')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = "./myapp/static/images"
RESIZED_FOLDER = "./myapp/static/resized"
THUMBNAIL_FOLDER = "./myapp/static/thumbnails"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@upload.route('/newimage', methods=['POST'])
def upload_img():
    global UPLOAD_FOLDER

    if 'image' not in request.files:
        return 'No file found'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        email = request.cookies.get('email', '')
        session_id = request.cookies.get('session_id', '')
        description = request.form["description"]
        redirect_url = "http://52.221.228.19:8037/api/profile/me?nc=1"
        data = {'filename': file.filename, 'email': email, 'session_id': session_id, 'description': description}
        files = {'image': file}
        r = requests.post("http://127.0.0.1:9999/image/newimage", data=data, files=files)
        result = json.loads(r.content)
        if result['success']:
            return render_template("success_and_redirect.html",
                                   success_message="Your image is uploaded! ",
                                   redirect_url=redirect_url)
        else:
            return render_template("error.html",
                                   error_message=result["message"],
                                   redirect_url=redirect_url)
