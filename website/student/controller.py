from flask import Blueprint, render_template, request, redirect, flash
import website.models as models

student_bp = Blueprint('student', __name__)

@student_bp.route('/')
def home():
    return render_template("home.html")

@student_bp.route('/student')
def view_student():
    students = models.Students.list()
    return render_template("student.html", students = students)

@student_bp.route('/student/add', methods = ['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        data = request.form
        print (data)
    return render_template("add_student.html")