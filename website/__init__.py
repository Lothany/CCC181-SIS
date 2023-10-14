from flask import Flask
from flask_mysql_connector import MySQL
from .config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'

    from .auth import auth
    from .view import view
    
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    
    mysql.init_app(app)
    
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(view, url_prefix='/')
    
    return app