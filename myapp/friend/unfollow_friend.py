from flask import Blueprint
from flask import request
from flask import render_template
import requests
import json

unfollowfriend = Blueprint('unfollowfriend', __name__, url_prefix='/api/friend')


@unfollowfriend.route('/unfollow', methods=['GET'])
def unfollow():
    email = request.cookies.get('email', '')
    session_id = request.cookies.get('session_id', '')
    friend_email = request.args.get('friend_email','')
    redirect_url = "http://52.221.228.19:8037/api/friend/mine"
    data = {'email': email, 'session_id': session_id,"friend_email": friend_email}
    r = requests.post("http://127.0.0.1:9998/friend/unfollow", data=data)
    result = json.loads(r.content)

    if result['success']:
        return render_template("success_and_redirect.html",
                               success_message="Unfollow success .",
                               redirect_url=redirect_url)
    else:
        return render_template("error.html",
                               error_message=result["message"],
                               redirect_url=redirect_url)
