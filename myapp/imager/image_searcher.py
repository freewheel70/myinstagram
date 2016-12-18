from flask import Blueprint
from flask import request
from flask import render_template
import requests
import json
from myapp.contants import urls

search = Blueprint('search', __name__, url_prefix='/api/search')


@search.route('/image', methods=['POST'])
def search_img():
    keyword = request.form['key']
    email = request.cookies.get('email', '')
    session_id = request.cookies.get('session_id', '')

    data = {'keyword': keyword, 'email': email, 'session_id': session_id}
    r = requests.post("http://127.0.0.1:9999/image/search", data=data)
    result = json.loads(r.content)

    if result['success']:
        return render_template("search_result.html",
                               has_login=True,
                               username=result['username'],
                               email=email,
                               logout_url=urls.logout_url,
                               upload_url=urls.upload_url,
                               profile_url=urls.profile_url,
                               keyword=keyword,
                               images=result['images'])
    else:
        return render_template("error.html",
                               error_message=result["message"],
                               redirect_url=urls.profile_url)