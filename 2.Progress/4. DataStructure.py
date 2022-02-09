## 介绍Python 常用的数据结构一些常用方法
# 0.zip 使用 zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9, 0]
print(list(zip(list1, list2)))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip(list1, list3)))  # [(1, 7), (2, 8), (3, 9)] 元素个数与最短的列表一致
print(dict([(1, 7), (2, 8), (3, 9)]))  # {1: 7, 2: 8, 3: 9}
# 1. 将两个列表转为字典
dict1 = dict()
print(dict1)
print(dict(zip(['name', 'age'], ['justin', 18])))  # {'name': 'justin', 'age': 18}
# 将元组列表转为字典
print(dict([('name', 'justin'), ('age', 19)]))  # {'name': 'justin', 'age': 19}
# 2.冻结集合 创建一个不可修改的集合
# forzenset( )，是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法
frozenset([1, 2, 3, 4, 5])
frozenset([1, 2, 3])
# 3.转为集合类型返回一个set对象，集合内不允许有重复数据
a = [1, 2, 3, 4, 4, 2, 3]
print(set(a))  # {1, 2, 3, 4}
print(type(set(a)))  # <class 'set'>
# 4.创建一个空的set 对象, 创建空的set 对象必须使用 set() {} 是创建了一个空的字典
set1 = {}
print(type(set1))  # <class 'dict'>
set2 = set()
print(type(set2))  # <class 'set'>
set3 = dict()
print(type(set3))  # <class 'dict'>
# 5.创建slice 对象
list1 = [_ for _ in range(10)]
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slice_New = slice(0, 10, 2)
print(list1[slice_New])  # [0, 2, 4, 6, 8]
# 6.转元组 tuple() 将对象转为一个不可变的序列类型
i_am_list = [2, 4, 6];
i_am_tuple = tuple(i_am_list)
print(i_am_tuple)  # (2, 4, 6)
