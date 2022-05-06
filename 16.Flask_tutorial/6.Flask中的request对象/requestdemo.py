# Flask 中的请求对象
from flask import Flask, request, render_template

app = Flask(__name__)


# 1.获取URL相关参数
# 2.解析查询参数
# 3.解析表单参数
# 4.解析json 数据

def echo(key, value):
    print('%-10s =%s' % (key, value))


@app.route('/ajax')
def ajax():
    return render_template('ajax.html')


@app.route('/')
def index():
    return render_template('index.html')


# 1.获取URL相关参数
@app.route('/query')
def query():
    echo('url', request.url)  # url       =http://127.0.0.1:5000/helloworld?name=张三
    echo('base_url', request.base_url)  # base_url  =http://127.0.0.1:5000/helloworld
    echo('host', request.host)  # host      =127.0.0.1:5000
    echo('host_url', request.host_url)  # host_url  =http://127.0.0.1:5000/
    echo('path', request.path)  # path      =/helloworld
    echo('full_path', request.full_path)  # full_path =/helloworld?name=张三
    print()
    echo('args', request.args)  # args      =ImmutableMultiDict([('name', '张三')])
    # 获取参数
    echo('args', request.args['name'])  # args      =张三
    return 'hello world'


# 2.解析查询参数
# http://127.0.0.1:5000/search?name=张三&age=12
@app.route('/search')
def search():
    name = request.args['name']
    age = request.args['age']
    echo('name', name)
    echo('age', age)
    return f"name is {name} age is {age}"


# 3.解析表单参数
@app.route('/form', methods=['post'])
def get_form():
    name = request.form['username']
    pwd = request.form['pwd']
    if name == 'justin' and pwd == '123':
        return 'login success'
    else:
        return 'login fail'


# 4.解析json 数据
@app.route('/api/addUser', methods=['post'])
def get_json():
    name = request.get_json().get('name')
    age = request.get_json().get('age')
    print('name',name)
    print('age',age)
    return f"name is {name} age is {age}"


if __name__ == '__main__':
    app.run()
