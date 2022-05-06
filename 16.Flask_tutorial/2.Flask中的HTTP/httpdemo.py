from flask import Flask, request,redirect,url_for

app = Flask(__name__)


@app.route('/login')
def login():
    return """
   <form action='/check_login' method='post'>
   <p><input type='text' name='name'></p>
   <p><input type='password' name='pwd'></p>
   <p><button type='submit'>提交</button></p>
   </form>
   """


@app.route('/check_login', methods=['post'])
def check_login():
    # 获取表单提交数据
    name = request.form['name']
    pwd = request.form['pwd']
    if name == 'justin' and pwd == '123':
        return 'login success'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
