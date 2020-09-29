import os
from flask import Flask
from flask import render_template, jsonify, send_from_directory
from flask_mongoengine import MongoEngine

db = MongoEngine()


def page_not_found(e):
    return render_template('404.html'), 404


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)

    @app.route('/static/<path:filename>')
    def staticfiles(filename):
        return send_from_directory(app.config["STATIC FOLDER"], filename)

    from project.home import home_blueprint
    from project.tracker import tracker_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(tracker_blueprint)

    app.register_error_handler(404, page_not_found)

    return app
