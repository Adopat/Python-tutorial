from sqlalchemy import Column,Integer,String
from app2 import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine(DB_URI,echo=True)

# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)
class User(Base):
    # 定义表名为users
    __tablename__ = 'users'

    # 将id设置为主键，并且默认是自增长的
    id = Column(Integer,primary_key=True)
    # name字段，字符类型，最大的长度是50个字符
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(100))

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return "<User(id='%s',name='%s',fullname='%s',password='%s')>" % (self.id,self.name,self.fullname,self.password)
# 2.映射到数据库中
Base.metadata.create_all()
# 3.添加数据到表
Session = sessionmaker(bind=engine)
session = Session()
ed_user = User(name='ed',fullname='Ed Jones',password='edspassword')
session.add(ed_user)
session.commit()
# 查找数据
for instance in session.query(User):
    print(instance)


