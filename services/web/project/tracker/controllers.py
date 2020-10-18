from flask import Blueprint, render_template
from flask_login import current_user, login_required
from project.utils import account_list_to_df
from project import logger
from datetime import datetime

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
@login_required
def index():
    user = current_user
    worth = account_list_to_df(user.worth)
    cash_flow = account_list_to_df(user.cash_flows)
    logger.info(worth.columns)
    logger.info(cash_flow)
    return render_template('tracker/main.html',
                           user=user,
                           worth=worth,
                           cash_flow=cash_flow)
