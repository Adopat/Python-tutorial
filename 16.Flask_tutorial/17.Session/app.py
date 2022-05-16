from flask import Flask, session, render_template
import os

app = Flask(__name__)
# SECRET_KEY
# 是一个密钥，Flask
# 以及相关的扩展
# extension
# 需要进行加密时需要使用到这个密钥，使用
# Session
# 存储数据时，Flask
# 在内部需要进行加密处理。
# 函数 os.urandom (24) 生成一个包含 24 个字符的随机字符串
app.config['SECRET_KEY'] = os.urandom(24)


def query():
    # session['user'] 和 session.get('user') 的区别,如果变量 user 不存在，session.get (‘user’) 返回 None，不会抛出异常,seesion['user']会抛出异常
    user = session.get('user')
    # user = session['user']
    return render_template('query.html', user=user)


@app.route('/set')
def set():
    session['user'] = 'justin'
    return query()


@app.route('/get')
def get():
    return query()


@app.route('/delete')
def delete():
    session.pop('user')
    return query()


@app.route('/clear')
def clear():
    session.clear()
    return query()


if __name__ == '__main__':
    app.run(debug=True)
