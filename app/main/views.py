from flask import render_template,redirect,abort,url_for,request
from . import main
from ..auth.forms import UpdateProfileForm
from .. import db, photos
from flask_login import login_required, current_user
from ..models import User,Pitch,Comment
from .forms import PitchForm, CommentForm
import markdown2

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
    pitches = Pitch.query.filter_by(author = user).all()

    if user is None:
        abort(404)
    return render_template('profile/profile.html', user = user, pitches = pitches)

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
        pitch = Pitch(title = form.title.data, content = form.content.data, category = form.category.data, user_id = current_user.id)
        pitch.save_pitch()

        return(redirect(url_for('.index')))

    return render_template('pitch/new_pitch.html', form = form)


@main.route('/pitch/<category>')
def pitch_category(category):
    '''
    Function to get and return template to view numerous categories
    '''
    pitches = Pitch.query.filter_by(category = category).all()
    return render_template('pitch/pitch_categories.html', pitches = pitches)

@main.route('/pitch/comment/new/<pitch_id>', methods = ['GET', 'POST'])
@login_required
def comment(pitch_id):
    '''
    Function to Implement comment on a pitch
    '''
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content = form.content.data, user_id = current_user.id, pitch_id = pitch_id)
        comment.save_comment()

        return(redirect(url_for('.view_pitch', pitch_id = pitch_id)))
    
    return render_template('pitch/comment.html', form = form, pitch = pitch)

@main.route('/pitch/view/<pitch_id>')
def view_pitch(pitch_id):
    '''
    Function to view pitches
    '''
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('pitch/pitch.html', pitch = pitch, comments = comments)