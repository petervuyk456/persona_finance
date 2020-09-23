from flask import Flask, render_template, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Bundle, Environment

db = SQLAlchemy()
migrate = Migrate()
assets_env = Environment()

main_css = Bundle(
    'css/bootstrap.css',
    filters='cssmin',
    output='css/common.css'
)

main_js = Bundle(
    'js/jquery.js',
    'js/bootstrap.js',
    filters='jsmin',
    output='js/common.js'
)


def page_not_found(e):
    return render_template('404.html'), 404


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/static/<path:filename>')
    def staticfiles(filename):
        return send_from_directory(app.config["STATIC FOLDER"], filename)

    from project.main import main_blueprint
    from project.tracker import tracker_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(tracker_blueprint)

    app.register_error_handler(404, page_not_found)

    return app
