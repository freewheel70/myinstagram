from flask import Blueprint
from flask import request
from flask import render_template
import requests
import json

remove = Blueprint('remove', __name__, url_prefix='/api/remove')


@remove.route('/image', methods=['POST'])
def remove_img():
    image = request.form['image']
    email = request.cookies.get('email', '')
    session_id = request.cookies.get('session_id', '')
    redirect_url = "http://52.221.228.19:8037/api/profile/me?nc=1"
    data = {'image': image, 'email': email, 'session_id': session_id}
    r = requests.post("http://127.0.0.1:9999/image/remove", data=data)
    result = json.loads(r.content)

    if result['success']:
        return render_template("success_and_redirect.html",
                               success_message="The image is removed! ",
                               redirect_url=redirect_url)
    else:
        return render_template("error.html",
                               error_message=result["message"],
                               redirect_url=redirect_url)