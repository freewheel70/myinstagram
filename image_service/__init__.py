from flask import Flask
from image_uploader import upload
from image_remover import remove
from image_searcher import search

image_handler = Flask(__name__)
image_handler.register_blueprint(upload)
image_handler.register_blueprint(remove)
image_handler.register_blueprint(search)