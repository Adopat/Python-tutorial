# 序列化和反序列化
import json


def get_stored_username():
    """如果存储了用户名，就获取它 反序列化"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            # 读取文件中的信息 存储到变量username 中
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名,序列化"""
    username = input("what is your name? ")
    filename = 'username.json'
    # 使用dump 将数据转存到文件username.json 函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，指出起名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
