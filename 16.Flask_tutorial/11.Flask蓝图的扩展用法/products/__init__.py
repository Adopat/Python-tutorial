from flask import Blueprint, render_template

# 指定template_folder 和 static_folder
blueprint = Blueprint('products', __name__, url_prefix='/product/', template_folder='templates', static_folder='static')


@blueprint.route('/car/')
def car_products():
    return '汽车板块'


@blueprint.route('/baby')
def baby_products():
    return render_template('baby.html')
