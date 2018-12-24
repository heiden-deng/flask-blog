import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abcdenfhfdsakfjksa'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'heiden <supports_robot@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    MAIL_DEFAULT_SENDER = 'supports_robot@163.com'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 994
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 994
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig, 'testing': TestingConfig, 'production': ProductionConfig,
    'default': DevelopmentConfig
}