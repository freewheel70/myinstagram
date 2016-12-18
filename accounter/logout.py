from flask import Blueprint
from flask import request
from session import remove_session
from session import find_session
import json

logout = Blueprint('logout', __name__, url_prefix='/logout')


@logout.route('/leave', methods=['POST'])
def log_out():
    email = request.form['email']
    session_id = request.form['session_id']
    current_session = find_session(email)
    if current_session['found'] and current_session['session_id'] == session_id:
        remove_session(email)
        return json.dumps({'success': True})
    else:
        return json.dumps({'success': False, 'message': 'invalid session'})
