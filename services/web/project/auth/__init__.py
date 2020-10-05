import functools
from flask import redirect, abort
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, AnonymousUserMixin, current_user, login_user


class TrackerAnonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"
login_manager.anonymous_user = TrackerAnonymous


def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .controllers import auth_blueprint
    app.register_blueprint(auth_blueprint)


def has_role(name):
    def real_decorator(f):
        def wraps(*args, **kwargs):
            if current_user.has_role(name):
                return f(*args, **kwargs)
            else:
                abort(403)
        return functools.update_wrapper(wraps, f)
    return real_decorator


@login_manager.user_loader
def load_user(user_id):
    from project.auth.models import User
    return User.objects.get(username=user_id)
