from . import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    '''
    Model class/db table for the user

    Args:
        db.Model: Connect our class to the database
    '''
    __tablename__  = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String())

    @property
    def password(self):
        '''
        Define property object to make limit access to pass_secure
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    '''
    Model class to specify one to many relationship

    Args:
        db.Model: Connect our class to the database
    '''

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String())
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    users = db.relationship('User', backref='pitch', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'
