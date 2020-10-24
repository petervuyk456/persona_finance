import os
from flask.cli import FlaskGroup

from project import db, create_app
from test_data import generate_users

env = os.environ.get('FLASK_ENV', 'development')
app = create_app('project.config.%sConfig' % env.capitalize())
cli = FlaskGroup(app)

from project.auth.models import User
from project import logger

@cli.command('create_collections')
def create_collections():

    generate_users(force=False)


@cli.command('run_tests')
def run_tests():
    logger.info("Starting tests...")
    # Put calls to test functions here

    logger.info("All tests passed")


if __name__ == "__main__":
    cli()
