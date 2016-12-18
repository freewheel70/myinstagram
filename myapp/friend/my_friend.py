from flask import Blueprint
from flask import request
from flask import render_template
import requests
import json
from myapp.contants import urls

myfriends = Blueprint('myfriends', __name__, url_prefix='/api/friend')


@myfriends.route('/mine', methods=['GET'])
def remove_img():
    email = request.cookies.get('email', '')
    session_id = request.cookies.get('session_id', '')
    redirect_url = "http://52.221.228.19:8037/api/profile/me"
    data = {'email': email, 'session_id': session_id}
    r = requests.post("http://127.0.0.1:9998/friend/mine", data=data)
    result = json.loads(r.content)

    if result['success']:
        return render_template("friend_list.html",
                               title="following list",
                               list_title="My Following",
                               friends=result['friends'],
                               has_login=True,
                               username=result['username'],
                               logout_url=urls.logout_url,
                               upload_url=urls.upload_url,
                               profile_url=urls.profile_url)
    else:
        return render_template("error.html",
                               error_message=result["message"],
                               redirect_url=redirect_url)
