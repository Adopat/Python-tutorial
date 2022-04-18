# 1. 局部变量
# def greet():
#     username = "zhiliao"
# print(username)

# 2. 全局变量
# username = "zhiliao"
# def greet():
#     print(username)
# greet()

# 3. global关键字
# 3.1. 如果在函数中，不使用global关键字，直接去修改全局变量的值，那么是不能修改的，而是创建了一个同名的参数
# 3.2. 如果想要修改，那么需要使用global [变量名]
# 3.3. 如果是容器类型（列表、字典），那么如果是添加元素，修改元素，是不需要使用global关键字的
# 但是如果是修改变量的一个指向，那么就需要使用global关键字
username = "zhiliao"
fruits = ['apple','banana']
def greet():
    # global username
    # username = "ketang"
    # fruits.append("orange")
    global fruits
    fruits = ['1']

print(fruits)
greet()
print(fruits)