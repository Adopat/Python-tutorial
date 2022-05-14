# 在视图函数中使用装饰器
from flask import Flask, request
from functools import wraps

app = Flask(__name__)


# 装饰器函数
def check_login(original_function):
    # 使用functools.wraps(original_function)保留原始函数original_function的属性。
    @wraps(original_function)
    def decorated_function(*args, **kwargs):
        user = request.args.get('user')
        if user and user == '张三':
            return original_function(*args, **kwargs)
        else:
            return '请登录'

    return decorated_function


# http://127.0.0.1:5000/page1?user=张三
@app.route('/page1')
@check_login
def page1():
    return 'page1'


if __name__ == '__main__':
    app.run(debug=True)
