from flask import Blueprint

auth = Blueprint('student', __name__)

@auth.route('/')
def home():
    return "<h1>home page</h1>"

@auth.route('/student')
def student():
    return "<p>student page</p>"

@auth.route('/course')
def course():
    return "<p>course page</p>"

@auth.route('/college')
def college():
    return "<p>college page</p>"
    
