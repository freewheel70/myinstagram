from flask import Blueprint
from flask import request
from flask import render_template
import requests
import json
from myapp.contants import urls

seefriend = Blueprint('seefriend', __name__, url_prefix='/api/friend')


@seefriend.route('/see', methods=['GET'])
def see_friend():
    email = request.cookies.get('email', '')
    session_id = request.cookies.get('session_id', '')
    friend_email = request.args.get('friend_email', '')

    data = {'email': email, 'session_id': session_id, "friend_email": friend_email}
    r = requests.post("http://127.0.0.1:9998/friend/see", data=data)
    result = json.loads(r.content)

    if result['success']:
        return render_template('friend_profile.html',
                               has_login=True,
                               username=result['username'],
                               email=email,
                               logout_url=urls.logout_url,
                               upload_url=urls.upload_url,
                               profile_url=urls.profile_url,
                               images=result['images'],
                               friendname=result['friendname'],
                               friendemail=friend_email,
                               is_friend=result['is_friend'])
    else:
        return render_template("error.html",
                               error_message=result["message"],
                               redirect_url=urls.profile_url)
