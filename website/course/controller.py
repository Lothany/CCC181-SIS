from flask import Blueprint, render_template, request
from . import models

course_bp = Blueprint('course',__name__)

@course_bp.route('/course')
def view_course():
    return render_template("course.html")

@course_bp.route('/add_course')
def add_course():
    return render_template("add_course.html")