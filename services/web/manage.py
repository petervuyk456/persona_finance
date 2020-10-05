import os
from flask.cli import FlaskGroup

from project import db, create_app
from project.auth.models import User

env = os.environ.get('FLASK_ENV', 'development')
app = create_app('project.config.%sConfig' % env.capitalize())
cli = FlaskGroup(app)


@cli.command('create_db')
def create_db():
    User.drop_collection()


@cli.command('seed_db')
def seed_db():
    admin1 = User(username='smyth', role='admin')
    user1 = User(username='holan', role='user')
    user2 = User(username='thegreat', role='user')
    admin1.set_password('12345671')
    user1.set_password('1234561')
    user2.set_password('abcd1234')
    admin1.save()
    user1.save()
    user2.save()

    user1.active_share.append(user2.id)
    user1.active_peek.append(user2.id)
    user2.active_share.append(user1.id)
    user2.active_peek.append(user1.id)
    user1.save()
    user2.save()


if __name__ == "__main__":
    cli()
