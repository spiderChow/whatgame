from datetime import datetime
from flask import render_template, session, redirect, url_for,request, jsonify

from . import main
from .forms import LoginForm
from .. import db
from ..models import User

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/howtoplay',methods=['GET','POST']) 
def how_to_play():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        user = User.query.filter_by(email=email).first()
        if user is None:
            if username is None or len(username)==0:
                flash('please name yourself!')
                return redirect(url_for('.how_to_play'))
            user = User(email=email,username=username)
            db.session.add(user)
            db.session.commit()
            session['known']=False
        else:
            session['known']=True

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

@main.route('/dump_sent')
def dump_sentence():
    pass