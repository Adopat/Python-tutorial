# Flaks 中的模板

# 1.分界符
# 2.变量
# 3.for 语句
# 4.if 语句
# 5.测试
# 6.过滤器

from flask import Flask, render_template

app = Flask(__name__)

string = 'aaaaaa'
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dic = {'name': 'justin', 'age': 12}


@app.route('/')
def index():
    return render_template('index.html', name='Justin', age=12)


@app.route('/index2')
def index2():
    return render_template('index2.html', string=string, list1=list1, dic=dic)


if __name__ == '__main__':
    app.run(debug=True)
