# 匿名函数：
# 1. 函数体只能有一行代码
# 2. 他会自动的把函数体的内容作为return返回回去，不需要写return
# 3. 用匿名函数的目的，就是不需要到其他地方额外定义一个函数，代码更加简洁

# persons = [{'username':'zhangsan','age':18},{"username":'lisi','age':25},{"username":'lisi','age':20}]
# def sort_key(item):
#     return item['age']
# persons.sort(key=lambda item:item['age'])
# print(persons)

def add(a,b):
    return a+b

def caculator(a,b,func):
    return func(a,b)

result = caculator(1,2,lambda x,y:x+y)
result = caculator(1,2,lambda x,y:x*y)
result = caculator(1,2,lambda x,y:x/y)
result = caculator(1,2,lambda x,y:x-y)
print(result)