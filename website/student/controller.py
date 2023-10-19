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
        studentID = data['studentID']
        firstName = data['firstName']
        lastName = data['lastName']
        courseCode = data['courseCode']
        yearLevel = data['yearLevel']
        gender = data['gender']
        
        if len(studentID) < 1:
            flash('Please enter student ID', category='error')
        elif len(firstName) < 1:
            flash('Please enter student first name', category='error')
        elif len(lastName) < 1:
            flash('Please enter student last name', category='error')
        elif courseCode == "empty":
            flash('Please choose a course', category='error')
        elif len(yearLevel) < 1:
            flash('Please enter student year level', category='error')
        elif not yearLevel.isdigit():
            flash('Year level must be a number between 1 and 6', category='error')
        elif not 1 <= int(yearLevel) <= 6:
            flash('Year level must be between 1 and 6', category='error')
        elif gender == "empty":
            flash('Please choose gender', category='error')
        else:
            student = models.Students(studentID, firstName, lastName, courseCode, yearLevel, gender)
            student.add()
            flash('Student added successfully!', category='success')
            return redirect('/student')
        
            #exists = student.add()
            #if exists == "duplicate":
            #    flash('Course with the same code already exists!', category='error')
            #else:
            #    flash('Course added successfully!', category='success')
            #    return redirect('/course')
    
    courses = models.Students.list_courses()
    return render_template('add_student.html', courses=courses)