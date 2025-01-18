from flask import Blueprint, render_template, request
from .auth import auth
from .auth import logged_in
from flask_login import login_required, current_user
from .models import Review
from sqlalchemy import *
from flask_sqlalchemy import *
from sqlalchemy.sql import *


db = SQLAlchemy()
views = Blueprint('views', __name__)
image = str
page_title = str
game_title = ["The Legend of Zelda: Breath of the Wild", 
"Celeste", 
"DRAGON BALL: Sparking! ZERO", 
"Dead Cells", "Eldin Ring", 
"Ghost of Tsushima", 
"Hollow Knight", 
"Minecraft", 
"Pokemon Black and White", 
"Sonic Adventure 2"]


@views.route('/')
def home():
    return render_template("home.html", page_title = "Home", user=current_user)



@views.route('/gamelist')
def gamelist():
    return render_template("gamelist.html", page_title = "Games List", user=current_user)



@views.route('/reviews')
def view_reviews():
    id = request.form.get('id')
    text = request.form.get('text')
    score = request.form.get('score')
    game = request.form.get('game')
    username = request.form.get('user_name')
    userid = request.form.get('user_id')
    review_amt = Review.query.count()
    reviews = Review.query.all()

    smt = select(Review).where(Review.id == 1)

    
    
    return render_template("reviews.html", page_title = "Reviews", user=current_user, Review=Review)



@views.route('/about')
def about():
    
    return render_template("about.html", page_title = "About", user=current_user)
