from flask import Flask
# __name__ 代表当前模块的名字
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<b>Hello World</b>'


if __name__ == '__main__':
    app.run()
    # 修改host 和端口号
    # app.run(host='0.0.0.0',port=23456)
