from flask import Blueprint

user_mod = Blueprint('user_mod', __name__, url_prefix='/api/user')


@user_mod.route('/<username>')
def get_user_profile(username):
    return "Hello "+username
# codes to retrieve a user profile
