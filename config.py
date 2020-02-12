import os

class Config:
    '''
    General configurations that are inherited by the other classes
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'

    # Email configurations

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    '''
    Configurations for application development phase
    '''
    pass

class DevConfig(Config):
    '''
    Configurations for when app is in development
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutugi:Mutugi@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

class TestConfig(Config):
    '''
    Configuration class for application testing
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutugi:Mutugi@localhost/pitch_test'
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
