from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from sqlalchemy import *

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Axolotl_Turtle_Frog_Elephant_Dinosaur'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .gameinfo import gameinfo

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(gameinfo, url_prefix='/gamelist')
    app.static_folder = 'STATIC'

    from .models import User, Review, Games

    with app.app_context():
        db.create_all()
        row_count = Games.query.count()

        if row_count != 10:
            db.session.add_all([
                Games(title='The Legend of Zelda: Breath of the Wild', image="botw.png"),
                Games(title='Celeste', image="celeste.png"),
                Games(title='DRAGON BALL: Ssparking! ZERO', image="dbsz.png"),
                Games(title='Dead Cells', image="deadcells.png"),
                Games(title='Eldin Ring', image="eldinring.png"),
                Games(title='Ghost of Tsushima', image="got.png"),
                Games(title='Hollow Knight', image="hollowknight.png"),
                Games(title='Minecraft', image="minecraft.png"),
                Games(title='Pokemon Black & White', image="bw.png"),
                Games(title='Sonic Adventure 2', image="sa2.png")
            ])
        db.session.commit()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
