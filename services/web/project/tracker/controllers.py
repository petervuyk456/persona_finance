from flask import Blueprint, render_template

tracker_blueprint = Blueprint(
    'tracker',
    __name__,
    template_folder='../templates',
    url_prefix="/tracker"
)


@tracker_blueprint.route('/')
def index():
    return render_template('tracker/main.html')
