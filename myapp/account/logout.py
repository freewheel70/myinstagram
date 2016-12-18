from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
import requests
import json

logout = Blueprint('logout', __name__, url_prefix='/api/logout')


@logout.route('/leave', methods=['GET'])
def log_out():
    email = request.cookies.get('email', '')
    session_id = request.cookies.get('session_id', '')
    payload = {'email': email, 'session_id': session_id}
    r = requests.post("http://127.0.0.1:6666/logout/leave", data=payload)
    result = json.loads(r.content)
    if result['success']:
        return redirect("http://52.221.228.19:8037/")
    else:
        return render_template("error.html",
                               message=result['message'],
                               redirect_url="http://52.221.228.19:8037/api")
