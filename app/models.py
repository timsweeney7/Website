#
#  This file is for defining 'classes' within the context of the website
#
#####################################################################
from app import db
from datetime import datetime
from app.forms import DeletePostForm


class ChatRoom:
    var = 'test'


class User:
    var = 'test'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    author = db.Column(db.String(64), index=True)
    text = db.Column(db.String(256), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    # delete_form = DeletePostForm

    def __repr__(self):
        return self.author + ': ' + self.text

