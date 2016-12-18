from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
import json
import requests
from flask import make_response

login = Blueprint('login', __name__, url_prefix='/api/login')


@login.route('/newuser', methods=['POST'])
def log_in():
    print "Login entry"
    print request.form.__dict__

    email = request.form['email']
    password = request.form['password']
    payload = {'email': email, 'password': password}
    r = requests.post("http://127.0.0.1:6666/login/newuser", data=payload)
    result = json.loads(r.content)
    if result["success"]:
        resp = make_response(redirect("http://52.221.228.19:8037/api/profile/me"))
        resp.set_cookie('email', email)
        resp.set_cookie('session_id', result["session_id"])
        return resp
    else:
        return render_template("error.html",
                               error_message=result["message"],
                               redirect_url="http://52.221.228.19:8037/api")
