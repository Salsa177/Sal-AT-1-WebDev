from flask import Blueprint, render_template

views = Blueprint('views', __name__)
image = str
game_title = []
game_info = []
game_platforms = []
game_release = str
page_title = str


@views.route('/')
def home():
    return render_template("home.html", page_title = "Home")



@views.route('/game-list')
def gamelist():
    return render_template("gamelist.html", page_title = "Games List")



