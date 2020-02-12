from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField, BooleanField, PasswordField, ValidationError
from wtforms.validators import Required, Email , EqualTo
from ..models import User, Pitch

class RegisterForm(FlaskForm):
    '''
    Form class to implement the user Registration form

    Args:
        FlaskForm: class from wtforms
    '''
    email = StringField('Email Address', validators = [Required(),Email()])
    username = StringField('Username', validators = [Required()])
    password = PasswordField('Password', validators = [Required(), EqualTo('password_confirmation', message= 'Passwords must match')])
    password_confirmation = PasswordField('Confirm Password', validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        '''
        Custom validator for user email
        '''
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is already an account with that email!')

    def validate_username(self,data_field):
        '''
        Custom validator for username
        '''
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is already taken!')
        
class LoginForm(FlaskForm):
    '''
    Class to implement user login form
    '''
    email = StringField('Email Address', validators = [Required(), Email()])
    password = PasswordField('Password', validators = [Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')

class UpdateProfileForm(FlaskForm):
    '''
    Class to implement update profile form
    '''
    bio = TextAreaField('Tell us about yourself!', validators=[Required()])
    submit =SubmitField('Update Profile')

