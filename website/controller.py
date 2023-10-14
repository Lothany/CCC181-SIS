from flask import Blueprint, render_template, request
import website.models as models

college_bp = Blueprint('college', __name__)

@college_bp.route('/college')
def display_college():
    colleges = models.Colleges.get_data()
    print(colleges)
    print("colleges retrieve")
    return render_template("college.html", colleges=colleges)