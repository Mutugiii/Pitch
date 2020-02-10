from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    Function to view the route page
    '''
    return render_template('index.html')
