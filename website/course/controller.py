from flask import Blueprint, render_template, request

course_bp = Blueprint('course',__name__)

@course_bp.route('/course')
def view_course():
    return render_template("course.html")

@course_bp.route('/add_course', methods = ['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        data = request.form
        print (data)
    return render_template("add_course.html")