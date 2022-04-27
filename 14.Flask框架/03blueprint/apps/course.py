from flask import Blueprint

bp = Blueprint("course",__name__,url_prefix="/course")

@bp.route("/list")
def course_list():
    return "课程列表"