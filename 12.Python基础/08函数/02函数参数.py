# 1. 形参与实参
# 1.1. 在函数定义的时候的参数就叫做形参
# 1.2. 在函数执行的时候实际传递进来的参数就叫做实参
# def add(a,b):
#     print(a+b)
#
# add(1,2)

# 2. 位置参数与关键字参数
# 2.2. 严格按照位置来传递的参数就叫做位置参数
# 2.3. 用形参赋值的方式传递的参数就叫做关键字参数
# def add(a,b):
#     print(f"a:{a}")
#     print(f"b:{b}")
#
# # add(1,2)
# add(b=1,a=2)

# 3. *args和**kwargs
# 3.1. *args：arguments，代表任意个数的位置参数
# 3.2. **kwargs：keyword arguments，代表任意个数的关键字参数
# 3.3. *args,**kwarg：组合起来，可以接收任意的参数
# 3.4. 在传实参的时候，位置参数必须要在关键字参数的前面

# def add(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     print(result)
# add(1,2,3,4,5,6,7,8,1)

# def info(**kwargs):
#     print(kwargs)
#
# info(name="zhiliao",age=18,height=180)

# def myfunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# myfunc(1,2,3,45,name="zhiliao",age=19)

x = (1,2)
def add(a,b):
    print(a+b)

# 如果想要将字典的key当做参数名字传进去，那么字典的key必须和参数的名称都保持一致
y = {"name":"zhiliao","age":18}
def greet(name,age):
    print(name,age)

# add(*x)
# greet(**y)

# 4. 默认参数
# 4.1. 默认参数可以不用传，如果没有传，那么就会使用默认指定的值
# 4.2. 如果传了，就会使用传的那个值
# 4.3. 如果某个参数没有默认值，那么这个参数就必须要传
# 4.4. 非默认参数必须要放到默认参数的前面，否则会报错
def greet(name,age=18):
    print(name,age)

greet("zhiliao")


