from project import logger
from flask_mongoengine import ValidationError
from mongoengine import MultipleObjectsReturned, DoesNotExist
import pandas as pd


def get_user(id_, username=None):

    from project.auth.models import User

    user_obj = None
    try:
        if username:
            user_obj = User.objects.get(username=username)
        elif id_:
            user_obj = User.objects.get(id=id_)
    except MultipleObjectsReturned:
        user_obj = User.objects(username)[0]
    except DoesNotExist:
        logger.warning("user or id does not exist in db")

    return user_obj


def account_list_to_df(accts):

    category = list()
    type_ = list()
    dates = list()
    values = dict()

    for acct in accts:
        category.append(acct.name)
        type_.append(acct.acct_type)
        for entry in acct.history:
            if entry.entry_date in values:
                values[entry.entry_date].append(entry.value)
            else:
                dates.append(entry.entry_date.strftime('%b %y'))
                values[entry.entry_date] = [entry.value]

    acct_df = pd.DataFrame(values, index=category)
    acct_df['Type'] = pd.Series(type_)
    acct_df.columns = ['Type']+dates
    return acct_df


def _not_empty(val):
    # Validates Mongo object field is not empty
    if not val:
        raise ValidationError('value can not be empty')
