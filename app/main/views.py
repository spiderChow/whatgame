from datetime import datetime
import re,string
from flask import render_template, session, redirect, url_for,request, jsonify, flash

from . import main
from .forms import LoginForm
from .. import db
from ..models import User, Sentence
import logging

logging.basicConfig(level=logging.INFO,filename='whatgame.log',format='%(asctime)s :%(levelname)s - %(message)s')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)




@main.route('/')
def home():
    return render_template('index.html')

@main.route('/howtoplay',methods=['GET','POST']) 
def how_to_play():
    form = LoginForm()
    logging.info(request.method)
    if form.validate_on_submit():
        # get data from POST
        email = request.form['email']
        username = request.form['username']
        # query the DB for the email
        user = User.query.filter_by(email=email).first()

        if user is None:
            # the user is new-comer
            if username is None or len(username)==0:
                # but fails to enter a name
                username = email.split("@")[0]
            # save the new-comer into DB
            logging.info(username)
            user = User(email=email,username=username)
            db.session.add(user)
            db.session.commit()
            
        #put the login user into session
        username = user.username
        session['username'] = username
        session['email'] = email
        logging.info(email+" log in named as " +username)

        return redirect(url_for('.play'))
    return render_template('how_to_play.html',form=form)


@main.route('/play')
def play():
    return render_template('play.html')


##################
##### three another ajax route methods
##################
@main.route('/_rank_list',methods=['POST'])
def rank_list():

    # user_id = request.args.get('user_id', 1, type=int)
    # get ranking list from DB
    l = User.query.order_by(User.score)
    l = [item.serialize for item in l.all()]
    l.reverse()
    #logging.info(l)
    return jsonify(ranklist=l)

@main.route('/user_info',methods=['POST'])
def user_info():
    user = User.query.filter_by(email=session['email']).first().serialize

    l = User.query.order_by(User.score)
    l = [item.serialize for item in l.all()]
    l.reverse()
    
    for rank ,item in enumerate(l):
        if item['email']==user['email']:
            break;
    
    return jsonify(user=user,rank=rank+1)

@main.route('/dump_sent' ,methods=['POST'])
def dump_sentence():
    # topic = request.args.get('topic-selected')
    # sentence = request.args.get('sentence')
    json = request.get_json()
    sentence = json['sentence']
    topic = json['topic']
    logging.info(topic+sentence)
    if topic is not None and len(topic)>0:
        if sentence is not None and len(sentence)>0:
            user = User.query.filter_by(email=session['email']).first()
            user_id = user.id
            sentence = Sentence(topic=topic, content=sentence, user_id=user_id)
            
            from app.main.similarity import similar 
            sim_sentence, cosine = similar(sentence.content)
            
            if cosine == 0 : # nonsense or very very special
                s = sentence.content
                trans = str.maketrans(string.punctuation,' '*len(string.punctuation))
                words = s.translate(trans).split()
                for w in words:
                    if not w.encode('UTF-8').isalpha():
                        return jsonify(success=4,score=user.score)
                
                return jsonify(success=3,score=user.score)
            else:
                if cosine > 0.9: # Good but the same with the db corpus
                    user.score = user.score+1
                    ret = jsonify(success=2,score=user.score)

                else:
                    this_score = round(10*(1/cosine)) if round(10*(1/cosine))<20 else 20
                    user.score = user.score+this_score
                    ret = jsonify(success=1,score=user.score)

                
                user.questionamount = user.questionamount+1
                
                
                db.session.add(sentence)
                db.session.add(user)
                db.session.commit()
                return ret
    return jsonify(success=0,score=0)

@main.route('/logout')
def logout():
    session.pop('username',None)
    session.pop('email',None)
    return redirect(url_for('main.home'))

