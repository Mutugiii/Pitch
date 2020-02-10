from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
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
    role_id = db.relationship('Review',backref='user', lazy='dynamic')
    pass_secure = db.Column(db.String())

    @property
    def password(self):
        '''
        Define property object to make limit access to pass_secure
        '''
        raise AttrbuteError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    '''
    Model class to specify one to many relationship

    Args:
        db.Model: Connect our class to the database
    '''

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'