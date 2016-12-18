from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import requests
import json

from myapp.account.login import login
from myapp.account.logout import logout
from myapp.account.profile import profile
from myapp.account.signup import signup
from myapp.imager.image_uploader import upload
from myapp.imager.image_remover import remove
from myapp.imager.image_searcher import search
from myapp.friend.all_friends import allfriends
from myapp.friend.my_friend import myfriends
from myapp.friend.follow_friend import followfriend
from myapp.friend.unfollow_friend import unfollowfriend
from myapp.friend.see_friend import seefriend

app = Flask(__name__)
app.secret_key = "ierg4080randomleehweerf"
app.register_blueprint(signup)
app.register_blueprint(login)
app.register_blueprint(profile)
app.register_blueprint(logout)
app.register_blueprint(upload)
app.register_blueprint(remove)
app.register_blueprint(search)
app.register_blueprint(allfriends)
app.register_blueprint(myfriends)
app.register_blueprint(followfriend)
app.register_blueprint(unfollowfriend)
app.register_blueprint(seefriend)


@app.route('/api')
def hello_world():
    email = request.cookies.get('email', '')
    session_id = request.cookies.get('session_id', '')

    if email == '' or session_id == '':
        return render_template("portal_form.html")

    payload = {'email': email, 'session_id': session_id, 'no_cache': False}
    r = requests.post("http://127.0.0.1:6666/profile/me", data=payload)
    result = json.loads(r.content)
    if result['loggedin']:
        return redirect("http://52.221.228.19:8037/api/profile/me")
    else:
        return render_template("portal_form.html")


if __name__ == '__main__':
    app.run()
