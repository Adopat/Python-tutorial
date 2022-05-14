from flask import Flask, render_template, request
import redis

app = Flask(__name__)
# decode_responses 使Redis 返回字符串
# 进入 redis 安装目录 redis-server redis.windows.conf 启动redis 服务
db = redis.Redis(host='127.0.0.1', decode_responses=True)


@app.route('/')
def index():
    return render_template('index.html')


# 查询数据
@app.route('/query', methods=['POST'])
def query():
    keys = db.keys()
    dicts = {}
    for key in keys:
        value = db.get(key)
        dicts[key] = value
    return render_template('query.html', dicts=dicts)


# 插入数据和修改数据
@app.route('/insert', methods=['post'])
@app.route('/update', methods=['post'])
def insert():
    key = request.form['key']
    value = request.form['value']
    db.set(key, value)
    return query()


@app.route('/insertMulti', methods=['post'])
def insertMulti():
    keyA = request.form['key1']
    print(keyA)
    valueA = request.form['value1']
    keyB = request.form['key2']
    valueB = request.form['value2']
    db.mset({keyA: valueA, keyB: valueB})
    return query()


# 删除数据
@app.route('/delete', methods=['post'])
def delete():
    key = request.form['key']
    db.delete(key)
    return query()


@app.route('/deleteAll', methods=['post'])
def deleteAll():
    db.flushall()
    return query()


if __name__ == '__main__':
    app.run(debug=True)
