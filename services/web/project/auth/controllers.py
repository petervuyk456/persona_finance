from flask import render_template, Blueprint, url_for, flash, redirect
from flask_login import login_user, logout_user, current_user

from project.auth.models import db, User
from project.auth.forms import LoginForm, RegisterForm

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates',
    url_prefix='/auth'
)

home_url = 'home.index'


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(home_url))

    form = LoginForm()

    if form.validate_on_submit():
        user = User(username=form.username.data)
        login_user(user, remember=form.remember.data)

        flash(f"Welcome {form.username.data}!", category="success")
        return redirect(url_for(home_url))

    return render_template('auth/login.html', form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You have been logged out. Come back soon!", category="success")
    return redirect(url_for(home_url))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)

        new_user.save()

        flash(
            f"User {form.username.data} has been created, please login.", category="success")
        return redirect(url_for('.login'))

    return render_template('auth/register.html', form=form)
