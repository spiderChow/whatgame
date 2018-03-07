# html form
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from flask_bootstrap import Bootstrap

# extends FlaskForm
class LoginForm(FlaskForm):
    # first para is label
    email = StringField('Email')
    username = StringField('name')
    submit = SubmitField('Go to play')

# class SentenceForm(FlaskForm):
#     topic = SelectField(
#         'topics',
#         choices=[('Finance', 'Finance'), ('ORM', 'ORM'), ('Sales', 'Sales')]
#     )
#     sentence = StringField('Try to type a question here.')
#     submit = SubmitField('Submit')

