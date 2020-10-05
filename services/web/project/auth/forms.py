from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, URL
from project.auth.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(max=64)])
    password = PasswordField(
        'Password', [DataRequired(), Length(min=6, max=255)])
    remember = BooleanField("Remember Me")

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        if not check_validate:
            return False

        user = User.objects.get(username=self.username.data)
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True


class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(max=64)])
    password = PasswordField(
        'Password', [DataRequired(), Length(min=6, max=255)])
    confirm = PasswordField('Confirm Password', [
                            DataRequired(), EqualTo('password')])

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        try:
            user = User.objects.get(username=self.username.data)
            if user:
                self.username.errors.append(
                    "User with that name already exists")
                return False
        except:
            return True
