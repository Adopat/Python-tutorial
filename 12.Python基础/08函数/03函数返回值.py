# 注意：只要return语句执行了，那么后面的代码就不会再执行了，这个函数就相当于结束了
# 函数如果要返回多个值，那么可以通过元组返回回去，然后外面调用函数的地方，可以通过元组解包的形式获取返回值
def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result
    print(result)

# x = add(1,2,3,4,5,6,7,8,9)
# print(x)

# def myfunc(age):
#     if age > 18:
#         return True
#     else:
#         print("未成年")
#         return False
#
# myfunc(16)

def myfunc(name,age):
    name += "_class"
    age += 1
    return name,age

name,age = myfunc("zhiliao",18)
print(name,age)