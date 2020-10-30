from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, URL
from project.tracker.models import Account, CashFlow, ACCT_TYPES, CF_TYPES

# TODO
# For each cf and acct need to check the following
# 1. acct/cf type is in acct_types or cf_types
# 2. acct/cf name does not already exist for user and is an option

class AddCashFlow(FlaskForm):
    cf_name = StringField('Cash Flow Name', [DataRequired(), Length(max=64)])
    cf_type = StringField('Cash Flow Type', [DataRequired(), Length(max=64)])

    def validate(self):
        check_validate = super(AddCashFlow, self).validate()

        if not check_validate:
            return False
        
        return True

class AddAccount(FlaskForm):
    acct_name = StringField('Account Name', [DataRequired(), Length(max=64)])
    acct_type = StringField('Cash Flow Type', [DataRequired(), Length(max=64)])

    def validate(self):
        check_validate = super(AddAccount, self).validate()

        if not check_validate:
            return False

        return True