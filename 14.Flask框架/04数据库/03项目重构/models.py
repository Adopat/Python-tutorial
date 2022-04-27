from exts import db

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