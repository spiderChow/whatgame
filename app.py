# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py
# for DB
app.config['SECRET_KEY'] = 'i am junying zhou' # protect the FORM from CSRF; TODO: need to be saved into ENV 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xswqaz@localhost:3306/whatgame'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)



class Sentence(db.Model):
    __tablename__ = 'sentences'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    # user_id = db.Column(db.Integer, nullable=False) # foreign key???
    topic = db.Column(db.String(20), nullable=False, server_default='')
    content = db.Column(db.String(100), nullable=False, server_default='')
    # relationship:
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return '<SEN %r>' % self.content

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    email = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    username = db.Column(db.String(32), nullable=False, server_default='', index=True)
    score = db.Column(db.Integer, nullable=False, server_default='0')
    questionamount = db.Column(db.Integer, nullable=False, server_default='0')
    # relationship
    sentences = db.relationship('Sentence',backref='sentence')

    def __repr__(self):
        return '<User %r,Email %r>' %(self.username,self.email)

    def __init__(self,email,username):
        self.email = email
        self.username = username
        self.score = 0
        self.questionamount = 0


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
           'email' : self.email,
           'username' : self.username,
           'score' : self.score,
           'questionamount' : self.questionamount
        }

# html form
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
Bootstrap(app)

# extends FlaskForm
class LoginForm(FlaskForm):
    # first para is label
    email = StringField('Email address')
    username = StringField('Nickname')
    submit = SubmitField('Go to play')




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/howtoplay',methods=['GET','POST']) 
def how_to_play():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        user = User.query.filter_by(email=email).first()
        if user is None:
            if username is None or len(username)==0:
                flash('please name yourself!')
                return redirect(url_for('how_to_play'))
            user = User(email=email,username=username)
            db.session.add(user)
            db.session.commit()
            session['known']=False
        else:
            session['known']=True

        return redirect(url_for('play'))
    return render_template('how_to_play.html',form=form)

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/_rank_list')
def rank_list():
    user_id = request.args.get('user_id', 1, type=int)
    # get ranking list from DB
    l = User.query.order_by(User.score)
    l = [item.serialize for item in l.all()]
    l.reverse()
    return jsonify(json_list=l)

@app.route('/dump_sent')
def dump_sentence():
    pass

"""
note for mysql installation:
  sudo apt-get install libmysqlclient-dev
  sudo apt-get install python-dev
  sudo python setup.py install

mysql_config: command not found

"""

if __name__ == '__main__':
    app.run()