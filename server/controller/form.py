from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    email = StringField('email', [DataRequired(), Email()])
    password = StringField('password', [DataRequired(), Length(min=5, max=20)])
    name = StringField('name', [DataRequired(), Length(min=2)])
    major = StringField('major', [DataRequired()])
