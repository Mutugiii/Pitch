from flask import render_template, url_for, redirect, flash, request
from . import auth,forms
from .forms import RegisterForm,LoginForm
from ..models import User
from flask_login import login_user,logout_user,login_required

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    '''
    Function to deal with user login 
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.query.filter_by(email = login_form.email.data).first()
        if user is not none and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember_data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')

    title = 'Pitch login'
    return render_template('auth/login.html', title = title, form = login_form)

@auth.route('/register', methods=['GET','POST'])
def register():
    '''
    Function to register new users
    '''
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    title = 'Pitch Register'
    return render_template('auth/register.html', form = form)


@auth.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated():
        username = current_user.username
    logout_user()
    return render_template('logout.html', username = username)    
