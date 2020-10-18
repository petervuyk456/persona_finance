from project import db
from project.constants import ACCT_TYPES, CF_TYPES
from project.utils import _not_empty
import datetime


class Entry(db.EmbeddedDocument):
    value = db.FloatField(min_value=0)
    entry_date = db.DateTimeField(default=datetime.datetime.utcnow)
    modified_date = db.DateTimeField(default=datetime.datetime.utcnow)


class Account(db.EmbeddedDocument):
    name = db.StringField(maxlength=64,
                          validation=_not_empty)
    acct_type = db.StringField(maxlength=24,
                               validation=_not_empty,
                               choices=ACCT_TYPES.keys())
    history = db.ListField(db.EmbeddedDocumentField(Entry))


class CashFlow(db.EmbeddedDocument):
    name = db.StringField(maxlength=64,
                          validation=_not_empty)
    acct_type = db.StringField(maxlength=24,
                               validation=_not_empty,
                               choices=CF_TYPES.keys())
    history = db.ListField(db.EmbeddedDocumentField(Entry))
