from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    Function to view the route page
    '''
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    '''
    Function to route to the profile page
    '''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)