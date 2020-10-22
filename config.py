import os
import json
basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv


# import environment variables
load_dotenv()

# Opening JSON file 
with open('credentials.json', 'r') as openfile: 
    POSTGRES = json.load(openfile)

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "odun omo oba"
    #SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEBUG = True
    DEVELOPMENT=True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True