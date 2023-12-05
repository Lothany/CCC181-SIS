from flask import Flask
from flask_mysql_connector import MySQL
from .config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, CLOUD_NAME, API_KEY, API_SECRET
import cloudinary

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_HOST=DB_HOST,
        MYSQL_DATABASE='sis181'
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    
    # cloudinary.config(
    #     cloud_name='dg9adkoyb',
    #     api_key= '983515472883825',
    #     api_secret='XGn8SzTJonIGDz59fUo-4MQ-wHA'
    # )
    
    cloudinary.config(
        cloud_name= CLOUD_NAME,
        api_key= API_KEY,
        api_secret= API_SECRET
    )
    
    mysql.init_app(app)

    
    from .student.controller import student_bp
    app.register_blueprint(student_bp, url_prefix="/")
    
    from .course.controller import course_bp
    app.register_blueprint(course_bp, url_prefix="/")
    
    from .college.controller import college_bp
    app.register_blueprint(college_bp, url_prefix="/")
    
    return app