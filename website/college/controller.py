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
        elif len(collegeName) < 1:
            flash('Please enter college name', category = 'error')
        else:
            college = models.Colleges(collegeCode, collegeName)
            exists = college.add()
            if exists == "duplicate":
                flash('College with same code already exists!', category = 'error')
                return render_template("add_college.html")
            else:    
                flash('College added succesfully!', category = 'success')
                return redirect ("/college")
    return render_template("add_college.html")

@college_bp.route('/college/edit', methods=['GET', 'POST'])
def edit_college():
    if request.method == 'POST':
        collegeCode = request.form.get('collegeCode')
        collegeName = request.form.get('collegeName')
        originalCode = request.args.get('collegeCode')

        college = models.Colleges(collegeCode, collegeName)
        exists = college.edit(originalCode)
        if exists == "duplicate":
            flash('College with the same code already exists!', category='error')
        elif len(collegeCode) < 1:
            flash('Please enter college code', category = 'error')
        elif len(collegeName) < 1:
            flash('Please enter college name', category = 'error')
        else:   
            flash('College edited successfully!', category='success')
            return redirect('/college')

    collegeCode = request.args.get('collegeCode')
    collegeName = request.args.get('collegeName')
    return render_template("edit_college.html", collegeCode=collegeCode, collegeName=collegeName)

@college_bp.route('/college/read', methods=['GET'])
def read_college():
    collegeCode = request.args.get('collegeCode')
    collegeName = request.args.get('collegeName')
    courses = models.Colleges.read(collegeCode)
    return render_template("read_college.html", collegeName=collegeName, courses=courses)


@college_bp.route('/college/delete', methods=['POST'])
def delete_college():
    if request.method == 'POST':
        collegeCode = request.form.get('collegeCode')
        college = models.Colleges(collegeCode)
        college.delete()
        flash('College deleted successfully!', category='success')
    return redirect('/college')

@college_bp.route('/college/search', methods=['GET', 'POST'])
def search_college():
    query = request.args.get('query')
    colleges = models.Colleges.search(query)
    return render_template("college.html", colleges=colleges)