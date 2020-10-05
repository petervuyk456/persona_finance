import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MONGODB_HOST = os.getenv(
        "DATABASE_URL", "mongodb+srv://dbUser:2YwlVplZsrhS9eOy@personafi.ofvfl.mongodb.net/Authentication?retryWrites=true&w=majority")
    STATIC_FOLDER = f'{os.getenv("APP_FOLDER")}/project/static'
    SEND_FILE_MAX_AGE_DEFAULT = 10
    SECRET_KEY = os.getenv("SECRET_KEY")
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')
    SECRET_KEY = '\xba\x00\x81\xb3\xd9\xef\x8cm\xcf\xa8\xbaF\xa2\xd6\x8c\xd2\xbd2\xba):\x98B\xe3'
    WTF_CSRF_SECRET_KEY = '\xb1\x91$[[Ou\x1d\xac\xa1\x03\x1cJ\xd7\xc6l\x02\x9bW\x1a>$T\x1b'


class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
