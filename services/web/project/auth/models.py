import datetime
from flask_login import UserMixin

from project import db, logger
from project.constants import ROLES
from project.auth import bcrypt, AnonymousUserMixin
from project.utils import _not_empty
from project.constants import ROLES
from project.tracker.models import Account, CashFlow
from project.utils import _not_empty


class User(UserMixin, db.Document):
    meta = {'collection': 'user'}
    username = db.StringField(max_length=64,
                              unique=True,
                              validation=_not_empty,
                              required=True)
    role = db.StringField(max_length=64,
                          validation=_not_empty,
                          default=ROLES[0],
                          choices=ROLES,
                          required=True)

    # Auth
    password = db.StringField(max_length=255, required=True)

    # Friends
    active_share = db.ListField(db.ReferenceField('self'))
    active_peek = db.ListField(db.ReferenceField('self'))
    temp_user = db.ListField(db.ReferenceField('self'))

    # PersonalFi Tracker
    worth = db.ListField(db.EmbeddedDocumentField(Account))
    cash_flows = db.ListField(db.EmbeddedDocumentField(CashFlow))

    # Meta Data
    last_login = db.DateTimeField()
    created_date = db.DateTimeField(default=datetime.datetime.utcnow)

    def __init__(self, username, role=ROLES[0], *args, **kwargs):
        super(db.Document, self).__init__(*args, **kwargs)
        self.username = username
        if role in ROLES:
            self.role = role

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def is_active(self):
        return True

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_anonymous(self):
        return not self.is_authenticated()

    def get_id(self):
        return self.username

    def has_role(self, name):
        if self.role == name:
            return True
        return False

    def set_password(self, password):
        if not isinstance(password, str):
            if isinstance(password, list):
                password = password[0]
            password = str(password)

        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        if isinstance(password, list) and password:
            password = password[0]

        if not self.password or not password:
            return False
        else:
            return bcrypt.check_password_hash(self.password.encode('utf-8'), password)
