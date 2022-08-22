from flask import Flask


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfsdfsdf'
    
    from .vievs import vievs
    from .auth import auth

    app.register_blueprint(vievs, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app