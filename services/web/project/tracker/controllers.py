from flask import Blueprint, render_template

tracker_blueprint = Blueprint(
    'tracker',
    __name__,
    template_folder='../templates/tracker',
    url_prefix="/tracker"
)


@tracker_blueprint.route('/')
def index():
    return render_template('main.html')
