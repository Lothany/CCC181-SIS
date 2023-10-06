from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'

    from .auth import auth
    from .view import view
    
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(view, url_prefix='/')
    
    return app