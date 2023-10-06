from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'

    from .student import student
    app.register_blueprint(student, url_prefix='/')
    
    return app