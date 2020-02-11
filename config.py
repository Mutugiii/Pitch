import os

class Config:
    '''
    General configurations that are inherited by the other classes
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')

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
