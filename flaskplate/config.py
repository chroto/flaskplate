import os

class BaseConfig(object):
    PROJECT = "flaskplate"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(
        os.path.dirname(__file__)
    ))

    DEBUG = False

    ADMINS = []
    SECRET_KEY = None  # Use os.urandom(32) to generate the Secret Key
    LOG_FOLDER = os.path.join(PROJECT_ROOT, 'logs')
    if not os.path.exists(LOG_FOLDER):
        os.mkdir(LOG_FOLDER)


class DefaultConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(DefaultConfig):
    pass

class TestConfig(DefaultConfig):
    pass


class ProductionConfig(BaseConfig):
    DEBUG = False
