# 使用 orm 进行增删改查

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

user = 'root'
password = 'root'
database = 'school'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建SQLAlchemy 对象 db
db = SQLAlchemy(app)


class Teacher(db.Model):
    # 将类Student 映射到表 students
    __tablename__ = 'teachers'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def dump(self):
        print(self.sno, self.name, self.age)


# 创建表
def create_table():
    db.drop_all()
    db.create_all()


def insert_teachers():
    tom = Teacher(sno=1, name='tom', age=12)
    db.session.add(tom)
    db.session.commit()
    jerry = Teacher(sno=2, name='jerry', age=11)
    mike = Teacher(sno=3, name='mike', age=11)
    justin = Teacher(sno=5, name='justin', age=12)
    db.session.add_all([jerry, mike, justin])
    db.session.commit()


def query_teachers():
    print('查询所有的老师')
    teachers = Teacher.query.all()
    for teacher in teachers:
        teacher.dump()
    print()
    print('查询所有年龄是 11 岁的老师')
    teachers = Teacher.query.filter_by(age=11)
    for teacher in teachers:
        teacher.dump()
    print()
    print('查询第一个年龄是11岁的老师')
    teachers = Teacher.query.filter_by(age=11)
    teacher = teachers.first()
    teacher.dump()
    print()
    print('查询姓名是 jerry 并且年龄是 11 岁的学生')
    teachers = Teacher.query.filter_by(age=11, name='jerry')
    for teacher in teachers:
        teacher.dump()
    print()


def update_teachers():
    teachers = Teacher.query.filter_by(name='tom')
    teachers.update({'name': 'TOM'})
    db.session.commit()


def delete_teachers():
    students = Teacher.query.filter_by(name='mike')
    students.delete()
    db.session.commit()


command = sys.argv[1]

command = sys.argv[1]
if command == 'create':
    create_table()
elif command == 'insert':
    insert_teachers()
elif command == 'query':
    query_teachers()
elif command == 'update':
    update_teachers()
elif command == 'delete':
    delete_teachers()
