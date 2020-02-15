from flask_wtf import FlaskForm
from wtforms import  StringField ,TextAreaField, SubmitField, SelectField
from wtforms.validators import Required
from ..models import Pitch, Comment

class PitchForm(FlaskForm):
    '''
    Class to implement the pitching form
    '''
    title = StringField('Pitch title', validators=[Required()])
    content = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('promotion','Promotion Pitch'), ('project','Project Pitch'), ('pickup','Pick Up lines')], validators=[Required()])
    submit = SubmitField('Post Pitch')

class CommentForm(FlaskForm):
    '''
    Form to comment on a pitch
    '''
    content = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Comment')