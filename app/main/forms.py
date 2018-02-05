# html form
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap

# extends FlaskForm
class LoginForm(FlaskForm):
    # first para is label
    email = StringField('Email address')
    username = StringField('Nickname')
    submit = SubmitField('Go to play')
