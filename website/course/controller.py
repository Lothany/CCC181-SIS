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
        courseCode = data['courseCode']
        courseName = data['courseName']
        college = data['college']
        
        if len(courseCode) < 1:
            flash('Please enter course code', category = 'error')
        elif len(courseName) < 1:
            flash('Please enter course name', category = 'error')
        else:
            course = models.Courses(courseCode, courseName, college)
            course.add()
            flash('Course added succesfully!', category = 'success')
            return redirect ("/course")
    
    return render_template("add_course.html")