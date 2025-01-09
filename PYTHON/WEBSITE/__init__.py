from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Axolotl_Turtle_Frog_Elephant_Dinosaur'

    from .views import views
    from .auth import auth
    from .gameinfo import gameinfo

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(gameinfo, url_prefix='/gamelist')
    app.static_folder = 'STATIC'

    return app
