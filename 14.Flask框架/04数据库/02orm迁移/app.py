from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zl_flask'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app,db)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200),nullable=False)
    # password = db.Column(db.String(200),nullable=False)


class UserExtension(db.Model):
    __tablename__ = "user_extension"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(100))
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    # db.backref
    # 1. 在反向引用的时候，如果需要传递一些其他的参数，那么就需要用到这个函数，否则不需要使用，只要在relationship的backref参数上，设置反向引用的名称就可以了。
    # 2. uselist=False：代表反向引用的时候，不是一个列表，而是一个对象。
    user = db.relationship("User",backref=db.backref("extension",uselist=False))


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)

    # 外键：
    # 1. 外键的数据类型一定要看，所引用的字段的类型
    # 2. db.ForeignKey("表名.字段名 ")
    # 3. 外键是属于数据库层面的，不推荐直接在ORM中使用
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    # relationship：
    # 1. 第一个参数是模型的名字，必须要和模型的名字保持一致
    # 2. backref（back reference）：代表反向引用，代表对方访问我的时候的字段名称
    author = db.relationship("User",backref="articles")


# 暂时还没有讲到ORM迁移数据库的版本管理，所以现在只能先删除所有表，再创建
# db.drop_all()
# db.create_all()


@app.route("/otm")
def one_to_many():
    article1 = Article(title="111",content="xxx")
    article2 = Article(title="222", content="yyy")
    user = User(username="zhiliao")
    article1.author = user
    article2.author = user
    db.session.add(article1,article2)
    db.session.commit()

    print(user.articles)
    return "one to many数据操作成功"


@app.route("/oto")
def one_to_one():
    user = User(username="zhiliao")
    extension = UserExtension(school="清华大学")
    user.extension = extension
    db.session.add(user)
    db.session.commit()
    return "one to one"


@app.route("/article")
def article_view():
    # 1. 添加数据
    # insert table article values(xx)
    # article = Article(title="钢铁是怎样炼成的",content="xxx")
    # db.session.add(article)
    # # 做一个提交操作
    # db.session.commit()

    # 2. 查询数据
    # filter_by：返回一个类列表的对象
    # article = Article.query.filter_by(id=1)[0]
    # print(article.title)

    # 3. 修改数据
    # article = Article.query.filter_by(id=1)[0]
    # article.content = "yyy"
    # db.session.commit()

    # 4. 删除数据
    Article.query.filter_by(id=1).delete()
    db.session.commit()
    return "数据操作成功"


@app.route('/')
def hello_world():
    # 写一个测试代码来验证是否连接成功
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
