# 定义元组
tuple = ()
# 具有一个项目的元组需要逗号
tuple = (3,)
# 定义一个元组
personInfo = ("Diana", 32, "New York")
# 数据存取
print("=====数据存取=====")
personInfo = ("Diana", 32, "New York")
print(personInfo[0])
print(personInfo[-1])
# 元组解包，一次分配多个变量
print("======元组解包======")
name, age, country, career = ("Diana", 32, "Canada", "CompSci")
print(career)
# 元组的追加
print("======元组的追加======")
x = (3, 4, 5, 6)
x = x + (1, 2, 3)
print(x)
