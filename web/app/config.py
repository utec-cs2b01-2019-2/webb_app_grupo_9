import os 


dbdir="sqlite:///" + os.path.abspath("/database.db")

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI="sqlite:///:memory"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY=".."

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = dbdir
    SECRET_KEY = os.environ["SECRET_KEY"]

class DevelopmentConfig(Config):
    