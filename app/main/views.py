from flask import render_template,redirect,abort,url_for,request
from . import main
from ..auth.forms import UpdateProfileForm
from .. import db, photos
from flask_login import login_required
from ..models import User,Pitch,Comment
from .forms import PitchForm

@main.route('/')
def index():
    '''
    Function to view the route page
    '''
    pitches = Pitch.query.all() 
    return render_template('index.html', pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    '''
    Function to route to the profile page
    '''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    pitches = Pitch.query.filter_by(user_id=user.id).all()
    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    '''
    Function to update user profile
    '''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfileForm()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form = form, user = user)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_picture(uname):
    '''
    Function for user to update profile picture
    '''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))
    

@main.route('/new/pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
    Function to create and save pitches in database
    '''
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title = form.title.data, content = form.content.data, category = form.category.data)
        db.session.add(pitch)
        db.session.commit()

        return(redirect(url_for('.index')))

    return render_template('pitch/new_pitch.html', form = form)


