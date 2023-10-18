from flask import Blueprint, render_template, request, redirect, flash
import website.models as models

college_bp = Blueprint('college',__name__)

@college_bp.route('/college')
def view_college():
    colleges = models.Colleges.list()
    return render_template("college.html", colleges = colleges)

@college_bp.route('/college/add', methods = ['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        data = request.form
        collegeCode = data['collegeCode']
        collegeName = data['collegeName']
        if len(collegeCode) < 1:
            flash('Please enter college code', category = 'error')
            return render_template("add_college.html")
        elif len(collegeName) < 1:
            flash('Please enter college name', category = 'error')
            return render_template("add_college.html")
        else:
            college = models.Colleges(collegeCode, collegeName)
            college.add()
            flash('College added succesfully!', category = 'success')
            return redirect ("/college")
    return render_template("add_college.html")

@college_bp.route('/college/delete', methods=['POST'])
def delete_college():
    if request.method == 'POST':
        collegeCode = request.form.get('collegeCode')
        college = models.Colleges(collegeCode)
        college.delete()
        flash('College deleted successfully!', category='success')
        return redirect('/college')
    return render_template("delete_college.html")
