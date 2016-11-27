from flask import Blueprint
from flask import render_template
from flask import session

profile = Blueprint('profile', __name__, url_prefix='/api/profile')


@profile.route('/me', methods=['GET'])
def see_profile():
    email = "Anonymous User"
    if 'email' in session:
        email = session['email']

    return render_template('profile.html',email = email)