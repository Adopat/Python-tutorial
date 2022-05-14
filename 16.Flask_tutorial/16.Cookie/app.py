from flask import Flask, request, Response, render_template

app = Flask(__name__)


# 在服务端获取 Cookie
@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('justin')
    return render_template('get_cookie.html', cookie=cookie)


# 设置cookie
@app.route('/set_cookie')
def set_cookie():
    # 获取页面模板的内容
    html = render_template('js_cookie.html')
    response = Response(html)
    # 产生一个 HTTP的 Set-Cookie消息头
    response.set_cookie('justin', 'www.justin.com')
    return response


@app.route('/del_cookie')
def del_cookie():
    html = render_template('js_cookie.html')
    response = Response(html)
    response.delete_cookie('justin')
    return response


if __name__ == '__main__':
    app.run(debug=True)
