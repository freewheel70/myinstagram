from flask import Flask
from myapp.account.login import login
from myapp.account.signup import signup
from myapp.account.profile import profile
from myapp.account.logout import logout
from user_mod import user_mod
from uuid import uuid4
from flask import session

app = Flask(__name__)
app.secret_key = "ierg4080randomleehweerf"
app.register_blueprint(user_mod)
app.register_blueprint(signup)
app.register_blueprint(login)
app.register_blueprint(profile)
app.register_blueprint(logout)


@app.route('/api')
def hello_world():
    if 'email' not in session:
        return "Anonymous user"
    else:
        return "Hello "+session['email']


if __name__ == '__main__':
    app.run()
