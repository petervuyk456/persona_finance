import os
import sys
import redis
import logging
from logging.config import dictConfig
from flask import Flask
from flask import render_template, jsonify, send_from_directory
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

db = MongoEngine()
login_mgr = LoginManager()
r = redis.Redis(host='redis', port=6379)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
logger = logging.getLogger(__name__)


def page_not_found(e):
    return render_template('404.html'), 404


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    login_mgr.init_app(app)

    @app.route('/static/<path:filename>')
    def staticfiles(filename):
        return send_from_directory(app.config["STATIC FOLDER"], filename)

    from project.auth import create_module as auth_create_module
    from project.home import create_module as home_create_module
    from project.tracker import create_module as tracker_create_module

    home_create_module(app)
    tracker_create_module(app)
    auth_create_module(app)

    app.register_error_handler(404, page_not_found)

    return app
