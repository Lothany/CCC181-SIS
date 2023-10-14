from flask import Flask
from flask_mysql_connector import MySQL

mysql = MySQL(app)

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'password'
    app.config['MYSQL_USER'] = "root"
    app.config['MYSQL_PASSWORD'] = "password123"
    app.config['MYSQL_DATABASE'] = "test"
    app.config['MYSQL_HOST'] = "localhost"
    
    mysql = MySQL(app)
    
    mysql = MySQL(app)
    mysql.init_app(app)

    from .auth import auth
    from .view import view
    
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(view, url_prefix='/')
    
    return app