#
#  This file is for defining 'classes' within the context of the website
#
#####################################################################
from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class ChatRoom:
    var = 'test'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return str(self.id) + '- ' + self.username


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    author = db.Column(db.String(64), index=True)
    text = db.Column(db.String(256), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return self.author + ': ' + self.text


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    file_name = db.Column(db.Text, index=True)
    mimetype = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())