import os
from flask.cli import FlaskGroup

from project import db, create_app
from project.tracker.models import User, Account

env = os.environ.get('FLASK_ENV', 'development')
app = create_app('project.config.%sConfig' % env.capitalize())
cli = FlaskGroup(app)


@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    db.session.add(User(username='peter', role="admin"))
    db.session.add(User(username='ali', role="user"))
    db.session.add(Account(name='401k', acct_type='asset'))

    db.session.commit()


if __name__ == "__main__":
    cli()
