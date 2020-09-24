from flask import Blueprint, render_template

home_blueprint = Blueprint(
    'home',
    __name__,
    template_folder='../templates',
)


@home_blueprint.route('/')
def index():
    return render_template('home/main.html')
