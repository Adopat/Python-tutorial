# 掌握常用的Python 编程习惯
# 1.理解 list 中 [] 和 None 的区别
print('======')
print(type(None)) # <class 'NoneType'> 空对象
print(type([])) # <class 'list'> 空列表
L1, L2 = None, []
print(bool(L1 == None)) # True
print(bool(L2 == [])) # True
print(bool(L1 is None)) # True
print(bool(L2 is None)) # False
# 2. 多余的空格
print('=====函数赋值以下符合习惯=====')
# foo(a, b=0, {'a':1, 'b':2}, (10,))
print('=====z增加函数原信息=====')
# def foo(x: int):
#     pass
# 是否为None 判断
print('=====判断某个对象是否为None的正确写法=====')
# if arr is None:
#     pass
# if arr is not None:
#     pass
print('=====对于list,tuple,set,dict,str等对象，使用下面方法判断是否为None更符合习惯=====')
# if not arr: # 为None 时满足条件
#     pass
# if arr： # 不为None时满足条件
#     pass
# lambda 表达式
# f = lambda i: i + 1 # 不推荐
# def is_add(i): return  i + 1 #符合习惯
