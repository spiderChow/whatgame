from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from flask_wtf import Form,FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


from config import config



bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'main.howtoplay'


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)

	# view and error-pages
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app