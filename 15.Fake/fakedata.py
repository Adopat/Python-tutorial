# 使用 fake 创建测试数据

# 连接 sqlserver 数据库
import pymssql
from faker import Faker

conn = pymssql.connect(host='172.18.21.125', user='test', password='Bb123456', database='test')
cursor = conn.cursor()

cursor = conn.cursor()
# 这里给出表结构，如果使用已存在的表，可以不创建表。
# sql = """
# CREATE TABLE test.dbo.userinfo (
#    id int primary key identity(1,1),
# 	username varchar(100) COLLATE Chinese_PRC_CI_AS NULL,
# 	phone varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	companyemail varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	email varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	company varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	address varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	street_address varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	city_name varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	city varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	province varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	postcode varchar(200) COLLATE Chinese_PRC_CI_AS NULL,
# 	country varchar(200) COLLATE Chinese_PRC_CI_AS NULL
# )
# """
# cursor.execute(sql)

fake = Faker("zh-CN")
# print(fake.simple_profile(sex=None))
# sql = """update test.dbo.userinfo set company ='兰金电子传媒有限公司666' where company ='兰金电子传媒有限公司'"""
for i in range(200000):
    sql = """insert into userinfo(username,phone,companyemail,email,company,address,street_address,city_name,city,province,postcode,country)
    values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" \
          % (fake.user_name(),
             fake.phone_number(),
             fake.company_email(),
             fake.email(),
             fake.company(),
             fake.address(),
             fake.street_address(),
             fake.city_name(),
             fake.city(),
             fake.province(),
             fake.postcode(),
             fake.country()
             )
    cursor.execute(sql)
    conn.commit()
# cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
