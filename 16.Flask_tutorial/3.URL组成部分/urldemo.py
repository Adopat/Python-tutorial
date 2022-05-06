from flask import Flask, request

app = Flask(__name__)


def echo(key, value):
    print('%-10s=%s' % (key, value))


# http://127.0.0.1:5000/helloworld?name=张三
@app.route('/helloworld')
def helloworld():
    """
    url
    base_url
    host
    host_url
    path
    full_path
    args
    :return:
    """
    echo('url', request.url)  # url       =http://127.0.0.1:5000/helloworld?name=张三
    echo('base_url', request.base_url)  # base_url  =http://127.0.0.1:5000/helloworld
    echo('host', request.host)  # host      =127.0.0.1:5000
    echo('host_url', request.host_url)  # host_url  =http://127.0.0.1:5000/
    echo('path', request.path)  # path      =/helloworld
    echo('full_path', request.full_path)  # full_path =/helloworld?name=张三
    print()
    echo('args', request.args)  # args      =ImmutableMultiDict([('name', '张三')])
    # 获取参数
    echo('args', request.args['name'])  # args      =张三
    return 'hello world'


if __name__ == '__main__':
    app.run()
