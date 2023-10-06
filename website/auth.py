from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/student')
def student():
    return "<p>student page</p>"

@auth.route('/course')
def course():
    return "<p>course page</p>"

@auth.route('/college')
def college():
    return "<p>college page</p>"
    
