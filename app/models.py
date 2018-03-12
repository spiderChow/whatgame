from . import db


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

