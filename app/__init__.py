from flask import Flask
from app.route import hello_world, index


def create_app():
    app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
    app.add_url_rule('/', '/', index)
    return app
