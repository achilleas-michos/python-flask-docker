import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'development_key'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
    'development': Development,
    'production': Production,
}

def get_config(environment):
    if environment in app_config:
        return app_config[environment]
    else:
        raise Exception('Configuration {} not recognized'.format(environment))

