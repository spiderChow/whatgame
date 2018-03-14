import os
basedir = os.path.abspath(os.path.dirname(__file__)) # get the abs path of the pj, e.g., '/home/chow/Documents/whatgame'

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess stringggggg'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
		'mysql+pymysql://root:xswqaz@127.0.0.1:3306/whatgame?charset=utf8' # TODO page67

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
		'mysql+pymysql://root:xswqaz@localhost:3306/testgame' # TODO page67

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
		'mysql+pymysql://root:xswqaz@localhost:3306/whatgame' # TODO page67

config = {
	'development' : DevelopmentConfig,
	'default' : DevelopmentConfig
}


