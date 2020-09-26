import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    STATIC_FOLDER = f'{os.getenv("APP_FOLDER")}/project/static'
    SEND_FILE_MAX_AGE_DEFAULT = 10


class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
