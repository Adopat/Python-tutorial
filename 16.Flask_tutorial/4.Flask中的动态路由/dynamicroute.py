# Flaks 中的动态路由和类型转换
from flask import Flask

app = Flask(__name__)


# 字符串
@app.route('/user/<name>')
def show_user(name):
    return f"name is  {name}"


# 整型
@app.route('/age/<int:age>')
def show_age(age):
    return f"age is {age}"


# 浮点型
@app.route('/price/<float:price>')
def show_price(price):
    return f"price is  {price}"


# 路径字符串
@app.route('/path/<path:name>')
def show_path(name):
    return f"path is  {name}"


if __name__ == '__main__':
    app.run()
