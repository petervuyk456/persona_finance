from flask import Blueprint, render_template

tracker_blueprint = Blueprint(
    'tracker',
    __name__,
    template_folder='../templates',
    url_prefix="/tracker"
)

ACTIVE_USERS = []
MONTHS = 5
PAGE_NUMBER = 1


@tracker_blueprint.route('/')
def index():
    return render_template('tracker/main.html')
