# 从flask包中导入Flask对象
from flask import Flask, jsonify, url_for, request, redirect
import config

# 使用Flask创建一个app对象，并且传递__name__参数
app = Flask(__name__)
# 以后所有的配置项都是放到config.py中

app.config.from_object(config)

books = [
    {"id": 1, "name": "三国演义"},
    {"id": 2, "name": "水浒传"},
    {"id": 3, "name": "红楼梦"},
    {"id": 4, "name": "西游记"}
]


# 1. 如果只是需要从服务器上获取数据，一般都是用GET请求
# 2. 如果前端需要把数据发送给服务器，一般用POST请求
# 3. 在@app.route上，添加methods参数，这个参数是一个列表类型，可以传递多个。
@app.route("/book/<string:book_id>", methods=['POST', 'GET'])
def book_detail(book_id):
    for book in books:
        if book_id == str(book['id']):
            return book

    return f"id为：{book_id}的图书没有找到！"


@app.route("/book/list")
def book_list():
    for book in books:
        book['url'] = url_for("book_detail", book_id=book['id'])
    return jsonify(books)


@app.route("/profile")
def profile():
    # 参数传递的两种形式：
    # 1. 作为url的组成部分：/book/1
    # 2. 查询字符串：/book?id=1
    user_id = request.args.get("id")
    if user_id:
        return "用户个人中心"
    else:
        return redirect(url_for("index"))


# @app.route：设置访问的url，这里是设置成一个根路径
@app.route('/')
def index():
    # return 'Hello 知了'
    return {"username": "知了"}


@app.route('/post/<string:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/url_for_test')
def url_for_test():
    return url_for('profile')


@app.route('/login')
def login():
    return 'login page'


@app.route('/get_login_name')
def get_login_name():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    else:
        return name





if __name__ == '__main__':
    app.run()
