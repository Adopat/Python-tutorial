# 蓝图 news.py
from flask import Blueprint
# 定义蓝图 指定 url
blueprint = Blueprint('news', __name__, url_prefix='/news')


@blueprint.route('/society/')
def society():
    return '社会新闻'


@blueprint.route('/tech/')
def tech_news():
    return 'IT技术新闻'
