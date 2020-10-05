from project import logger
from flask_mongoengine import ValidationError
from mongoengine import MultipleObjectsReturned, DoesNotExist


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


def _not_empty(val):
    # Validates Mongo object field is not empty
    if not val:
        raise ValidationError('value can not be empty')
