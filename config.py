import os

class Config:
    '''
    General configurations that are inherited by the other classes
    '''
    pass

class ProdConfig(Config):
    '''
    Configurations for application development phase
    '''
    pass

class DevConfig(Config):
    '''
    Configurations for when app is in development
    '''
    DEBUG = True

class TestConfig(Config):
    '''
    Configuration class for application testing
    '''
    pass

config_options = {
        'development': DevConfig,
        'production': ProdConfig,
        'test': TestConfig
}
