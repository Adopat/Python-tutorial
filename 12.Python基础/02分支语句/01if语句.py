# 1. 布尔类型（bool）
# 只有两个值，分别是True和False

# 2. if语句
# if False:
#     print("条件成立！")

# 3. 代码块：
# 3.1. 如果某个代码片段，是属于某个语句的，那就需要进行缩进，可以使用2个空格，4个空格，以及一个tab键
# 3.2. 如果需要指定说某个语句的代码块开始，那么就在这个的末尾加上一个英文的冒号
# 3.3. 只要取消缩进了，那么就意味着这个代码块结束了。

# if False:
#     print("条件成立！")
# print("运动")


# 4. else语句
# if False:
#     print("逛公园")
# else:
#     print("打游戏")


# 4. elif语句
# input函数接收到的所有数据都是字符串类型
age = input("请输入年龄：")
age = int(age)

if age == 18:
    print("刚成年")
elif age < 18:
    print("未成年")
else:
    print("已成年")