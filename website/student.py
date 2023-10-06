from flask import Blueprint

student = Blueprint('student', __name__)

@student.route('/')
def student_page():
    return "<h1>student page</h1>"
    
