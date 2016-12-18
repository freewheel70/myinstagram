from flask import Blueprint
from flask import render_template
import json
from flask import request
import requests

signup = Blueprint('signup', __name__, url_prefix='/api/signup')


@signup.route('/newuser', methods=['POST'])
def sign_up():
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    payload = {'email': email, 'password': password, 'username': username}
    r = requests.post("http://127.0.0.1:6666/signup/newuser", data=payload)
    result = json.loads(r.content)
    if result['success']:
        return render_template("success_and_redirect.html",
                               success_message="Sign up successfully, you can log in now !",
                               redirect_url="http://52.221.228.19:8037/")
    else:
        return render_template("error.html",
                               error_message=result["message"],
                               redirect_url="http://52.221.228.19:8037/api")
