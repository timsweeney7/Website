#
#  This file is for defining the web forms on the website
#
#####################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import URLField


class PostForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DeletePostForm(FlaskForm):
    button = SubmitField('Delete')

    @staticmethod
    def post_to_delete(self, id):
        self.id = id