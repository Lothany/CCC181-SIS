from flask import Blueprint, render_template, request
from website import mysql

auth = Blueprint('auth', __name__)

@auth.route('/student')
def student():
    return render_template("student.html")

@auth.route('/add_student', methods = ['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        data = request.form
        print (data)
    return render_template("add_student.html")

@auth.route('/course')
def course():
    return render_template("course.html")

@auth.route('/add_course', methods = ['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        data = request.form
        print (data)
    return render_template("add_course.html")

@auth.route('/college')
def college():
    return render_template("college.html")

@auth.route('/add_college', methods = ['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        college_data = request.form
        college = College(
            college_data['collegeCode'],
            college_data['collegeName']
        )
        college.add()
    return render_template("add_college.html")
    
