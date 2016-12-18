from flask import Blueprint
from flask import render_template
from flask import request
import requests
import json

profile = Blueprint('profile', __name__, url_prefix='/api/profile')


@profile.route('/me', methods=['GET'])
def see_profile():
    no_cache = (request.args.get('nc', 0) != 0)
    email = request.cookies.get('email', '')
    print "Profile access by " + email + " nc=" + str(no_cache)
    session_id = request.cookies.get('session_id', '')
    logout_url = "http://52.221.228.19:8037/api/logout/leave"
    upload_url = "http://52.221.228.19:8037/api/upload/newimage"
    profile_url = "http://52.221.228.19:8037/api/profile/me"

    payload = {'email': email, 'session_id': session_id, 'no_cache': no_cache}
    r = requests.post("http://127.0.0.1:6666/profile/me", data=payload)
    result = json.loads(r.content)
    if result['loggedin']:
        return render_template('profile.html',
                               has_login=True,
                               username=result['username'],
                               email=email,
                               logout_url=logout_url,
                               upload_url=upload_url,
                               profile_url=profile_url,
                               images=result['images'])
    else:
        return render_template("error.html",
                               error_message="Please Log in",
                               redirect_url="http://52.221.228.19:8037/api"
                               )
