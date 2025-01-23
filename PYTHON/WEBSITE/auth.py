from flask import Blueprint, render_template, request, flash, redirect, url_for, request
from .models import User, Review
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import GameSelectForm
from .models import Games
from sqlalchemy.sql import func
import datetime

auth = Blueprint('auth', __name__)
logged_in : bool = False
gameimage = ""

@auth.route('/logout')
def logout():
    flash('Logged out successfully', category='success')
    logout_user()
    logged_in = False
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                logged_in = True
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Account under that email does not exist', category='error')

    return render_template("login.html", user=current_user)



@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Account under that email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(username) < 2:
            flash('Username must be atleast 2 characters', category='error')
        elif len(password) < 7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            logged_in = True
            flash('Account created succesfully', category='success')
            return redirect(url_for('auth.login'))
            

    return render_template("signup.html", user=current_user)
    


@auth.route('/posting', methods=['GET', 'POST'])
@login_required
def post_reviews():

    form = GameSelectForm()

    if request.method == 'POST':
        review = request.form.get('review')
        score = request.form.get('score')
        title = request.form.get('title')
        username = current_user.username
        userid = current_user.id
        time = datetime.datetime.now()
        day = time.strftime("%d ")
        month = time.strftime("%b ")
        year = time.strftime("%Y")
        date = day + month + year
        print(date)

        selected_game = ""
        acceptable_score = ['0', '1', '2', '3', '4', '5']


        if form.games.raw_data == ['1']:
            selected_game = "The Legend of Zelda: Breath of the Wild"
        elif form.games.raw_data == ['2']:
            selected_game = "Celeste"
        elif form.games.raw_data == ['3']:
            selected_game = "DRAGON BALL: Sparking! ZERO"
        elif form.games.raw_data == ['4']:
            selected_game = "Dead Cells"
        elif form.games.raw_data == ['5']:
            selected_game = "Eldin Ring"
        elif form.games.raw_data == ['6']:
            selected_game = "Ghost of Tsushima"
        elif form.games.raw_data == ['7']:
            selected_game = "Hollow Knight"
        elif form.games.raw_data == ['8']:
            selected_game = "Minecraft"
        elif form.games.raw_data == ['9']:
            selected_game = "Pokémon Black and White"
        elif form.games.raw_data == ['10']:
            selected_game = "Sonic Adventure 2"

        if len(title) < 1:
            flash("Must provide a title", category='error')
        elif len(review) < 1:
            flash("Must provide a review", category='error')
            print(selected_game)
        elif len(score) < 1:
            flash("Must enter a score", category='error')
        elif score not in acceptable_score:
            flash("Score must be a number between 1 and 5", category='error')
        else:
            new_review = Review(text=review, game=selected_game, user_name=username, user_id=userid, score=int(score), title=title, date=date)
            db.session.add(new_review)
            db.session.commit()
            flash('Review posted', category='success')
            return redirect(url_for('views.home'))

    return render_template("post.html", user=current_user, gameimage="placeholder.png", form=form)





