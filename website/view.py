from flask import Blueprint, render_template, request

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return render_template("home.html")

@view.route('/student')
def student():
    return render_template("student.html")

@view.route('/add_student', methods = ['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        data = request.form
        print (data)
    return render_template("add_student.html")

@view.route('/course')
def course():
    return render_template("course.html")

@view.route('/add_course', methods = ['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        data = request.form
        print (data)
    return render_template("add_course.html")

@view.route('/college')
def college():
    return render_template("college.html")

@view.route('/add_college', methods = ['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        data = request.form
        print (data)
    return render_template("add_college.html")
    
