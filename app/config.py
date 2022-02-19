import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

    MAIL_SERVER = os.environ.get('smtp.mailtrap.io"', 'localhost')
    MAIL_PORT = os.environ.get('587 ', '25')
    MAIL_USERNAME = os.environ.get('effc80600feffb')
    MAIL_PASSWORD = os.environ.get('5802738d90ae34')
