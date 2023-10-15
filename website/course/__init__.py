from flask import Blueprint

course_bp = Blueprint('course',__name__)

from . import controller