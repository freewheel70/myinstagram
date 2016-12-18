from flask import Flask
from go_follow_friend import followfriend
from go_unfollow_friend import unfollowfriend
from go_see_friend import seefriend
from get_all_friends import allfriends
from get_my_friend import myfriends

friend_handler = Flask(__name__)
friend_handler.register_blueprint(followfriend)
friend_handler.register_blueprint(unfollowfriend)
friend_handler.register_blueprint(seefriend)
friend_handler.register_blueprint(allfriends)
friend_handler.register_blueprint(myfriends)