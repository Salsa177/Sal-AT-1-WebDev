from flask import Blueprint, render_template
from .auth import auth
from .auth import logged_in
from flask_login import login_required, current_user


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
    return render_template("home.html", page_title = "Home",)



@views.route('/gamelist')
def gamelist():
    return render_template("gamelist.html", page_title = "Games List")



@views.route('/reviews')
def view_reviews():
    return render_template("reviews.html", page_title = "Reviews")



@views.route('/about')
def about():
    return render_template("about.html", page_title = "About")
