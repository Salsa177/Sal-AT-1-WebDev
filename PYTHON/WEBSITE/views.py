from flask import Blueprint, render_template, request
from .auth import auth
from .auth import logged_in
from flask_login import login_required, current_user
from .models import *
from sqlalchemy import *
from flask_sqlalchemy import *
from sqlalchemy.sql import *
from WEBSITE import db




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



@views.route('/reviews', methods=['GET', 'POST'])
def view_reviews():
    row = 0
    reviews = db.session.query(Review).all()
    review_count = len(reviews)
    print(review_count)
    

    
    return render_template("reviews.html", page_title = "Reviews", user=current_user, 
                           reviews=reviews, row=row, review_count=review_count
                           )


@views.route('/about')
def about():
    
    return render_template("about.html", page_title = "About", user=current_user)


