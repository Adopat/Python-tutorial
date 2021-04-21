# 1. 创建空列表
a = []
# 2.访问元素 使用下标
# 3. 添加元素 append()
# 4. 删除元素 remove(),pop(),del
a = [1,2,3,4,5,1]
a.remove(1)
print(a) # [2, 3, 4, 5, 1] 使用remove() 删除列表中的元素，只能删除重复出现元素的第一个
a = [1,2,3,4,5,1]
a.pop()
print(a) # 默认删除最后一个元素 pop
a = [1,2,3,4,5,1]
a.pop(0)
print(a) # [2, 3, 4, 5, 1] pop(a) 带参数的话删除指定位置的元素
# del 与 pop 类似，删除指定索引处的元素 del 必须带参数
a = [1,2,3]
del a[0]
print(a) # [2, 3]
# 5. list 与 in
# 6. list 与数字
print(['Hi']*4) # ['Hi', 'Hi', 'Hi', 'Hi'] 实现元素的复制
# 使用列表和数字相乘构建二维列表
a = [[]]*3
a[0] = [1,2]
a[1] = [3,4]
a[2] = [5,6]
print(a)
# 7.列表生成式
# 8.其他常用方法 clear,index,count,sort,reverse,copy
a = [1,2,3,4,5]
print("删除前：",a) # 删除前： [1, 2, 3, 4, 5]
a.clear()
print('删除后：',a) # 删除后： []
# index 用于查找某个元素的索引
a = [1,2,3,4,5,1]
print(a.index(5)) # 4
# count 用于统计某个元素出现的次数
a = [1,2,3,4,5,1]
print(a.count(1)) # 2
# sort 对list 进行排序，对原list 进行排序，不生成新的list,sorted() 对所有可迭代对象进行排序，生成新的list,不对原始list 改变
a = [(3,1),(4,1),(1,3),(5,4),(9,-10)]
a.sort(key= lambda x :x[1])
print(a) # [(9, -10), (3, 1), (4, 1), (1, 3), (5, 4)]
# reverse 实现列表反转
a = [1,2,3,4,5]
a.reverse()
print(a) # [5, 4, 3, 2, 1]
# 9. 列表实现栈 栈是一种只能在列表一端进出的特殊列表
stack = [1,3,5]
stack.append(0)
print(stack)
stack.pop()
print("pop后的列表 ：",stack)
# 10 .列表包含自身 a[1]-->中间元素-->a[1]
a = [1,2,3]
a[1] = a
print(a)
# 11. 列表插入元素性能差，凡是涉及频繁插入删除元素的操作都不适合 list
# 12.Python 的深拷贝 deepcopy 浅拷贝 copy 浅拷贝只拷贝一层
a = [1,2,3]
ac = a.copy()
print('ac=',ac)
print('a=',a)
print("对浅拷贝的ac进行操作")
ac[2]=4
print('ac=',ac) # ac= [1, 2, 4]
print('a=',a) # 可以看出对浅拷贝得到的对象进行修改并不会对原始对象进行改变 #a= [1, 2, 3]
print("======浅拷贝只拷贝一层======")
a = [[1,2],[3,4]]
ac = a.copy()
print('修改前：',ac)
ac[1] =[4,5]
print('修改后：',ac) # [[1, 2], [4, 5]]
print('修改后:',a) # [[1, 2], [3, 4]]
print("=====另一种情况=====")
a = [[1,2],[3,4]]
ac = a.copy()
print('原始a =:',a)
print('原始ac =:',ac)
ac[1][1] =5
print('ac= ',ac) # ac=  [[1, 2], [3, 5]]
print('a =',a) # a = [[1, 2], [3, 5]] 可以看到浅拷贝对原始数据进行了改变
print('=====deepcopy=====')
import copy
a = [[1,2],[3,4]]
ac = copy.deepcopy(a)
print('修改前 ac：',ac) # [[1, 2], [3, 4]]
ac [1][1] =5
print('修改后 ac',ac) # [[1, 2], [3, 5]]
print('修改后 a',a) # [[1, 2], [3, 4]] 可以看到进行深层拷贝后 并不会对原始list 进行修改

# 13. 列表是可变的，可变对象是不可哈希的，不可哈希的对象是不能映射，因此不能被用作字典的键，元组是不可变的，可将list 转为元组，用作字典的键

# a = [1,3]
# d = {a:'不能被哈希'} # unhashable type: 'list'









