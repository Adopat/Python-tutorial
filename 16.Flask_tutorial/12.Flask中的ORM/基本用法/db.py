from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = 'root'
password = 'root'
database = 'school'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建SQLAlchemy 对象 db
db = SQLAlchemy(app)


# 建立类与表之间的映射
class Student(db.Model):
    # 将类Student 映射到表 students
    __tablename__ = 'students'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)


# 使用面向对象的语法访问数据库
students = Student.query.all()
for stu in students:
    print(stu.sno, stu.name, stu.age)
