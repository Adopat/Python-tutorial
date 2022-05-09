# 过滤器的使用
# 1.常见的过滤器
#      字符串操作
#      列表操作
#      其他常用的过滤器
# 2.自建过滤器
from flask import Flask, render_template

app = Flask(__name__)

input = 123


def increase(input):
    output = input + 1
    return output


app.add_template_filter(increase, 'increase')


@app.template_filter('decrease')
def decrease(input):
    output = input - 1
    return output


@app.route('/')
def index():
    return render_template('index.html', input=input)


if __name__ == '__main__':
    app.run(debug=True)
