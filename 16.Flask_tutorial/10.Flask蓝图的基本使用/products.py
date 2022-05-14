from flask import Blueprint

blueprint = Blueprint('product.css', __name__, url_prefix='/product.css')


@blueprint.route('/car/')
def car_products():
    return '汽车板块'


@blueprint.route('/baby')
def baby_products():
    return '婴儿产品板块'
