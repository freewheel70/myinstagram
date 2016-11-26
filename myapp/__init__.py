from flask import Flask
from myapp.account.login import login
from myapp.account.signup import signup
from user_mod import user_mod

app = Flask(__name__)
app.register_blueprint(user_mod)
app.register_blueprint(signup)
app.register_blueprint(login)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
