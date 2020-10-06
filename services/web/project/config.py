import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MONGODB_HOST = os.getenv("DATABASE_URL")
    STATIC_FOLDER = f'{os.getenv("APP_FOLDER")}/project/static'
    SEND_FILE_MAX_AGE_DEFAULT = 10
    SECRET_KEY = os.getenv("SECRET_KEY")
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')


class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
