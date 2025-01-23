from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000))
    score = db.Column(db.Integer)
    game = db.Column(db.String(1000))
    user_name = db.Column(db.String(150))
    user_id = db.Column(db.Integer)
    date = db.Column(db.String(2000))
    title = db.Column(db.String(50))
    
class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
