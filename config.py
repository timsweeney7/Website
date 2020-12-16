#
#  This file is for setting the configuration of your application
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
    UPLOAD_FOLDER = '/Users/timsweeney/Website/application/static'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS
