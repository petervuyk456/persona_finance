import os
from flask.cli import FlaskGroup

from project import db, create_app
from test_data import generate_td, reset_db

env = os.environ.get('FLASK_ENV', 'development')
app = create_app('project.config.%sConfig' % env.capitalize())
cli = FlaskGroup(app)


@cli.command('create_db')
def create_db():
    reset_db()
    # pass


@cli.command('seed_db')
def seed_db():
    generate_td()
    # pass


if __name__ == "__main__":
    cli()
