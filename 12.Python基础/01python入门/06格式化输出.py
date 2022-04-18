
# 1. 用%的方式格式化输出
# 整形：%d
# 浮点类型：%f，如果想要指定保留小数点后多少位，那么就可以在%后加一个.number，比如%.2f就是保留两位小数
# 字符串类型：%s

# name = input("请输入姓名：")
# print("my name is %s"%name)

# age = 18
# print("my age is %d"%age)

# price = 18.495483
# print("the apple's price is %.2f"%price)

# name = "zhiliao"
# age = 18
# print("my name is %s,my age is %d"%(name,age))

# name = "zhiliao"
# age = 18
# price = 3.56
# print("my name is %s,my age is %s,the apple's price is %s"%(name,age,price))

# 2. 用f-string
# 推荐使用f-string：更加方便、更加直观、执行效率比%的形式更高。
name = "zhiliao"
age = 18
# print(f"my name is {name}, my age is {age}")


# 也可以直接把变量通过逗号的形式拼接到字符串中进行输出
print('my name is',name,'my age is',age)