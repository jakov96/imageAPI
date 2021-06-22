import os

basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

POSTGRES_USER = os.environ.get('POSTGRES_DB_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_DB_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_DB_HOST')
POSTGRES_NAME = os.environ.get('POSTGRES_DB_NAME')


class Config:
    SECRET_KEY = "\xda\xb2\x95\xd72\xd5\xf5\t\x96\xfd\x1d'\xb4\xe8h\x0cO\x0b(N)>\x88\xde"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:5432/{3}'.format(
        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_NAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
