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
            exists = student.add()
            if exists == "duplicate":
                flash('Student ID is already taken', category='error')
            else:
                flash('Student added successfully!', category='success')
                return redirect('/student')
    
    courses = models.Students.list_courses()
    return render_template('add_student.html', courses=courses)

@student_bp.route('/student/edit', methods = ['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        studentID = request.form.get('studentID')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        courseCode = request.form.get('courseCode')
        yearLevel = request.form.get('yearLevel')
        gender = request.form.get('gender')
        trueStudent = request.args.get('studentID')
        
        student = models.Students(studentID, firstName, lastName, courseCode, yearLevel, gender)
        exists = student.edit(trueStudent)
        if exists == "duplicate":
            flash('Student ID is already taken', category='error')
        elif len(studentID) < 1:
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
            flash('Student edited successfully!', category='success')
            return redirect('/student')

        #exists = student.edit(trueStudent)
        #if exists == "duplicate":
        #    flash('Student ID is already taken', category='error')
       # else:   
        #    flash('Student edited successfully!', category='success')
        #    return redirect('/student')

    studentID = request.args.get('studentID')
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    course = request.args.get('courseCode')
    yearLevel = request.args.get('yearLevel')
    gender = request.args.get('gender')
    courses = models.Students.list_courses()
    return render_template(
        "edit_student.html",
        studentID = studentID,
        firstName = firstName,
        lastName = lastName,
        course = course,
        yearLevel = yearLevel,
        gender = gender,
        courses = courses
    )