from flask import Blueprint, render_template, request, redirect, flash
import website.models as models

course_bp = Blueprint('course',__name__)

@course_bp.route('/course')
def view_course():
    courses = models.Courses.list()
    return render_template("course.html", courses = courses)

@course_bp.route('/course/add', methods = ['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        data = request.form
        print (data)
    return render_template("add_course.html")