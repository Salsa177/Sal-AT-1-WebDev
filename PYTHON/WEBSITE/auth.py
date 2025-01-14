from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Review
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)
logged_in : bool = False

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

    return render_template("login.html")



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
            

    return render_template("signup.html")
    


@auth.route('/posting')
@login_required
def post_reviews():
    return render_template("post.html")


