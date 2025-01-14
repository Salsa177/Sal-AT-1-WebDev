from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    reviews = db.relationship('Review', primaryjoin="User.id == Review.user_id")

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    game = db.Column(db.Integer)
    user_name = db.Column(db.String(150), db.ForeignKey('user.username'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    