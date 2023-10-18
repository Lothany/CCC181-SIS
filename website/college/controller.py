from flask import Blueprint, render_template, request, redirect, flash
import website.models as models

college_bp = Blueprint('college',__name__)

@college_bp.route('/college')
def view_college():
    colleges = models.Colleges.list()
    return render_template("college.html", colleges = colleges)

#@college_bp.route('/add_college')
#def add_college():
#    return render_template("add_college.html")

@college_bp.route('/add_college', methods = ['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        data = request.form
        collegeCode = data['collegeCode']
        collegeName = data['collegeName']
        college = models.Colleges(collegeCode, collegeName)
        college.add()
        #return 'added succesfully'
        return redirect ("/college")
    return render_template("add_college.html")