from flask import render_template
from . import main

@main.app_errorhandler(404)
def error404(error):
    '''
    Function to deal with wrong routes in the blueprint
    '''

    return render_template('404.html'),404
