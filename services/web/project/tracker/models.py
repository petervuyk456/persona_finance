from project import db
from project.constants import ROLES, ACCT_TYPES, CF_TYPES
import datetime
from flask_mongoengine import ValidationError


acc_types = (t[0] for t in ACCT_TYPES)
cf_types = (t[0] for t in CF_TYPES)


def _not_empty(val):
    if not val:
        raise ValidationError('value can not be empty')


class Entry(db.EmbeddedDocument):
    value = db.FloatField(min_value=0)
    entry_date = db.DateTimeField(default=datetime.datetime.utcnow)
    modified_date = db.DateTimeField(default=datetime.datetime.utcnow)


class Account(db.EmbeddedDocument):
    name = db.StringField(maxlength=64,
                          validation=_not_empty)
    acct_type = db.StringField(maxlength=24,
                               validation=_not_empty,
                               choices=acc_types)
    history = db.ListField(db.EmbeddedDocumentField(Entry))


class CashFlow(db.EmbeddedDocument):
    name = db.StringField(maxlength=64,
                          validation=_not_empty)
    acct_type = db.StringField(maxlength=24,
                               validation=_not_empty,
                               choices=acc_types)
    history = db.ListField(db.EmbeddedDocumentField(Entry))


class User(db.Document):
    username = db.StringField(max_length=64,
                              unique=True,
                              validation=_not_empty)
    role = db.StringField(max_length=64,
                          validation=_not_empty,
                          default="user",
                          choices=ROLES)
    created_date = db.DateTimeField(default=datetime.datetime.utcnow)
    worth = db.ListField(db.EmbeddedDocumentField(Account))
    cash_flows = db.ListField(db.EmbeddedDocumentField(CashFlow))
