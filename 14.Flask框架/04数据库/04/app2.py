# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'dashdemo'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)