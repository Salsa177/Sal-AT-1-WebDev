from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)
logged_in : bool = False

@auth.route('/login')
def login():
    return '<p>login<p>'



@auth.route('/logout')
def logout():
    return '<p>logout<p>'



@auth.route('/sign-up')
def sign_up():
    if logged_in:
        return '<p>sign up<p>'
    

@auth.route('/posting')
def post_reviews():
    if logged_in == True:
        return render_template("post.html")
    else:
        return login()


