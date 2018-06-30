import os

base_dir = os.path.abspath(os.path.dirname(__file__))
database = os.path.join(base_dir, "database.db")

class Config(object):

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "ass"
