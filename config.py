import os

basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SOMESUPERSECRETKEY'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'ducetrak.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
