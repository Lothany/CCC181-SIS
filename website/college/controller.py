from flask import Blueprint, render_template, request
from . import models

college_bp = Blueprint('college',__name__)

@college_bp.route('/college')
def view_college():
    return render_template("college.html")

@college_bp.route('/add_college')
def add_college():
    return render_template("add_college.html")