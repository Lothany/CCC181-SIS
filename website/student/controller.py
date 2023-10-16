from flask import Blueprint, render_template, request

student_bp = Blueprint('student', __name__)

@student_bp.route('/student')
@student_bp.route('/')
def view_student():
    return render_template("student.html")

@student_bp.route('/add_student')
def add_student():
    return render_template("add_student.html")