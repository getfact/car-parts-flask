from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):

    name = TextAreaField("Name of the car part", validators=[DataRequired()])
    body = TextAreaField("Describe the car part", validators=[DataRequired()])
    submit = SubmitField("Submit")
