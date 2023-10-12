from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/student')
def student():
    return render_template("student.html")

@auth.route('/add_student')
def add_student():
    return render_template("add_student.html")

@auth.route('/course')
def course():
    return render_template("course.html")

@auth.route('/add_course')
def add_course():
    return render_template("add_course.html")

@auth.route('/college')
def college():
    return render_template("college.html")

@auth.route('/add_college')
def add_college():
    return render_template("add_college.html")
    
