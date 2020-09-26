import datetime
from project import db

accounts = db.Table('accounts',
                    db.Column('user_id', db.Integer, db.ForeignKey(
                        'user.id'), primary_key=True),
                    db.Column('account_id', db.Integer, db.ForeignKey(
                        'account.id'), primary_key=True)
                    )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    role = db.Column(db.String(64), nullable=False, default="user")
    created_date = db.Column(db.DateTime(), default=datetime.datetime.now)
    accounts = db.relationship('Account', secondary=accounts, lazy='subquery',
                               backref=db.backref('users', lazy=True))

    def __init__(self, username, role="user"):
        self.username = username
        self.role = role

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    acct_type = db.Column(db.String(24), nullable=False)
    history = db.Column(db.PickleType())

    def __init__(self, name, acct_type):
        self.name = name
        self.acct_type = acct_type
