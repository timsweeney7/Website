#
#  This file is for setting the configuration of your app
#
#####################################################################
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DefaultConfig(object):
    DEBUG = True
    SECRET_KEY = 'qwertyuiopasdfghjklzxcvbnm'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False