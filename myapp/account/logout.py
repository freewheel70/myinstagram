from flask import Blueprint
from flask import request
from flask import render_template
from flask import session

logout = Blueprint('logout', __name__, url_prefix='/api/logout')


@logout.route('/leave', methods=['POST', 'GET'])
def log_out():
    if request.method == 'GET':
        return render_template('logout.html')
    else:
        if request.method == 'POST':
            session.pop('email', None)
            return "Log out Successful"
        else:
            return "Invalid Method"