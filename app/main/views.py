from datetime import datetime
from flask import render_template, session, redirect, url_for,request, jsonify, flash
from flask_login import login_required
from flask.ext.login import login_user,logout_user, current_user

from . import main
from .forms import LoginForm
from .. import db
from ..models import User, Sentence


@main.route('/')
def home():
    return render_template('index.html')

@main.route('/howtoplay',methods=['GET','POST']) 
def how_to_play():
    form = LoginForm()
    print(request.method)
    if form.validate_on_submit():
        email = request.form['email']
        username = request.form['username']
       
        user = User.query.filter_by(email=email).first()
        if user is None:
            # the user is new-comer
            if username is None or len(username)==0:
                # but fails to enter a name
                username = email.split("@")[0]
                print(email)
                print(username)
            user = User(email=email,username=username)
            db.session.add(user)
            db.session.commit()
            session['known']=False
        else:
            # the user is already met 
            session['known']=True

        login_user(user) # mark the user as logined in the user session
        return redirect(url_for('.play'))
    return render_template('how_to_play.html',form=form)


@main.route('/play')
def play():
    return render_template('play.html')

@main.route('/_rank_list')
def rank_list():
    user_id = request.args.get('user_id', 1, type=int)
    # get ranking list from DB
    l = User.query.order_by(User.score)
    l = [item.serialize for item in l.all()]
    l.reverse()
    return jsonify(json_list=l)

@main.route('/dump_sent' ,methods=['POST'])
def dump_sentence():
    # topic = request.args.get('topic-selected')
    # sentence = request.args.get('sentence')
    json = request.get_json()
    sentence = json['sentence']
    topic = json['topic']
    print(topic+sentence)
    if topic is not None and len(topic)>0:
        if sentence is not None and len(sentence)>0:

            session['topic'] = topic
            session['sentence'] = sentence

            user_id = current_user.id
            sentence = Sentence(topic=topic, content=sentence, user_id=user_id)
            

            from app.main.similarity import similar 
            sim_sentence, cosine = similar(sentence.content)

            user = current_user
            user.questionamount = user.questionamount+1
            
            

            if cosine == 0 :
                user.score = user.score + 0
                return jsonify(success=2,score=user.score)
            else:
                user.score = user.score+round(10*(1/cosine))
                
                db.session.add(sentence)
                db.session.add(user)
                db.session.commit()
                return jsonify(success=1,score=user.score)

    return jsonify(success=0,score=0)

@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logout!')
    return redirect(url_for('main.home'))