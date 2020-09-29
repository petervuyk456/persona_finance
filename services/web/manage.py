import os
from flask.cli import FlaskGroup

from project import db, create_app
from project.tracker.models import User

env = os.environ.get('FLASK_ENV', 'development')
app = create_app('project.config.%sConfig' % env.capitalize())
cli = FlaskGroup(app)


@cli.command('create_db')
def create_db():
    for user in User.objects:
        user.delete()


@cli.command('seed_db')
def seed_db():
    User(username='peter', role="admin").save()
    User(username='ali', role="user").save()


if __name__ == "__main__":
    cli()
