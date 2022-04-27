from sqlalchemy import create_engine

# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'dashdemo'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# 创建数据库引擎
engine = create_engine(DB_URI)

# 创建连接
with engine.connect() as con:
    rs = con.execute('SELECT 1')
    print(rs.fetchone())
# 使用sqlalchemy 操作原生SQL
with engine.connect() as con:
    # 先删除 authors表
    con.execute('drop table if exists authors')
    con.execute('create table authors(id int primary key, auto_increment varchar(50), name varchar(25))')
    # 插入两条数据到表中
    con.execute('insert into authors(id,name) values(1,"abc")')
    con.execute('insert into authors(id,name) values(2,"xiaotuo")')
    # 执行查询操作
    results = con.execute('select * from authors')
    # 从查找的结果中遍历
    for result in results:
        print(result)
