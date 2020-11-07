#
#  This file is for defining the web forms on the website
#
#####################################################################

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import URLField


class CommentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DeleteCommentForm(FlaskForm):
    button = SubmitField('Delete')

    @staticmethod
    def comment_to_delete(self, id):
        self.id = id


class UploadFileForm(FlaskForm):
    #validators = [FileRequired()]
    file = FileField()
    button = SubmitField('Upload')
