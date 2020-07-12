#
#  This file is for defining the web forms on the website
#
#####################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit')
