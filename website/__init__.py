from flask import Flask
from flask_mysql_connector import MySQL
from .config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'
    
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    
    mysql.init_app(app)
    
    #from .view import view
    #app.register_blueprint(view, url_prefix='/')
    
    from .student.controller import student_bp
    app.register_blueprint(student_bp, url_prefix="/")
    
    from .course.controller import course_bp
    app.register_blueprint(course_bp, url_prefix="/")
    
    from .college.controller import college_bp
    app.register_blueprint(college_bp, url_prefix="/")
    
    return app