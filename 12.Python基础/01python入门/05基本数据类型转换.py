
# 1. 为什么需要做数据类型转换
# input函数：接收的任何数据，都是str类型。
# age = input("请输入你的年龄：")
# print(type(age))

# 2. 浮点、字符串转换为整形
# 2.1. 浮点类型转整形
# price = 12.9
# price1 = int(price)
# print(type(price))
# print(type(price1))

# 2.2. 字符串类型转整形
# 字符串转整形：如果字符串中出现了阿拉伯数字以外的其他任意字符，都会导致转换失败
# age = "23.4"
# age1 = int(age)
# print(type(age1))

# 3. 整形、字符串转换为浮点类型
# 3.1. 整形转浮点：
# price = 18
# price1 = float(price)
# print(type(price1))
# print(price1)

# 3.2. 字符串转浮点：字符串中只能出现阿拉伯数字以及小数点，否则就会失败
# price = "18.3"
# price1 = float(price)
# print(price1)
# print(type(price1))


# 4. 整形、浮点类型转换为字符串
# 4.1. 整形转字符串
# age = 18
# age1 = str(age)
# print(type(age1))

price = 18.4
price1 = str(price)
print(price1)
print(type(price1))