# 在视图类中使用装饰器
from flask import Flask, request, views
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
class Page1(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return 'page1'


# http://127.0.0.1:5000/page2?user=张三
class Page2(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return 'PAGE2'


app.add_url_rule(rule='/page1', view_func=Page1.as_view('page1'))
app.add_url_rule(rule='/page2', view_func=Page2.as_view('page2'))

if __name__ == '__main__':
    app.run(debug=True)
