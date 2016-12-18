from flask import Flask
from login import login
from logout import logout
from profile import profile
from signup import signup

account_handler = Flask(__name__)
account_handler.register_blueprint(signup)
account_handler.register_blueprint(login)
account_handler.register_blueprint(profile)
account_handler.register_blueprint(logout)
