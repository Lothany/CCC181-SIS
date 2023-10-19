from flask import Blueprint, render_template, request, redirect, flash
import website.models as models

course_bp = Blueprint('course',__name__)

@course_bp.route('/course')
def view_course():
    courses = models.Courses.list()
    return render_template("course.html", courses = courses)

@course_bp.route('/course/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        data = request.form
        courseCode = data['courseCode']
        courseName = data['courseName']
        collegeCode = data['collegeCode']
        
        if len(courseCode) < 1:
            flash('Please enter course code', category='error')
        elif len(courseName) < 1:
            flash('Please enter course name', category='error')
        elif collegeCode == "empty":
            flash('Please choose a college', category='error')
        else:
            course = models.Courses(courseCode, courseName, collegeCode)
            exists = course.add()
            if exists == "duplicate":
                flash('Course with the same code already exists!', category='error')
            else:
                flash('Course added successfully!', category='success')
                return redirect('/course')
    
    colleges = models.Courses.list_colleges()
    return render_template('add_course.html', colleges=colleges)

@course_bp.route('/course/edit', methods = ['GET', 'POST'])
def edit_course():
    if request.method == 'POST':
        courseCode = request.form.get('courseCode')
        courseName = request.form.get('courseName')
        collegeCode = request.form.get('collegeCode')
        trueCourse = request.args.get('courseCode')

        course = models.Courses(courseCode, courseName, collegeCode)
        exists = course.edit(trueCourse)
        if exists == "duplicate":
            flash('Course with the same code already exists!', category='error')
        else:   
            flash('Course edited successfully!', category='success')
            return redirect('/course')

    courseCode = request.args.get('courseCode')
    courseName = request.args.get('courseName')
    college = request.args.get('collegeCode')
    collegeList = models.Courses.list_colleges()
    return render_template("edit_course.html", courseCode=courseCode, courseName=courseName, college=college, collegeList = collegeList)

@course_bp.route('/course/delete', methods=['POST'])
def delete_course():
    if request.method == 'POST':
        courseCode = request.form.get('courseCode')
        course = models.Courses(courseCode)
        course.delete()
        flash('Course deleted successfully!', category='success')
    return redirect('/course')

@course_bp.route('/course/search', methods=['GET', 'POST'])
def search_course():
    query = request.args.get('query')
    courses = models.Courses.search(query)
    return render_template("course.html", courses=courses)