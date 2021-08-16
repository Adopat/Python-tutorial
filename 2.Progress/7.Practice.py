# 1.不用else if 实现计算器
from operator import *
def calculator(a,b,k):
    return {
        '+':add,
        '-':sub,
        '*':mul,
        '/':truediv,
        '**':pow,
        '//':floordiv, # 地板除(整除)
        '%':mod # 取余
    }[k](a,b)
print(calculator(5,6,'*')) # 30
print(calculator(6,5,'/')) # 1.2
print(calculator(6,5,'//')) # 1
print(calculator(6,5,'%')) # 1

print("==========")
test = [1,2,3,4]
print(test[0:4])
print(test[0:len(test)])
print(test[0:len(test)-1])


print("============")


# 2.去除数组最大值，求和
list1 = [1,2,3,6,4,5,7,9,8]
list1.sort()
list2 = list1[0:len(list1)-1]
print("list2",list2)
print(list1)
def sort_mean(lst):
    lst.sort()
    lst2 = lst[0:len(lst)-1]
    return sum(lst2)/len(lst2)

print(sort_mean([1,2,3,6,4,5,7,9,8]))
print(sum([1, 2, 3, 4, 5, 6, 7, 8]))
print(len([1, 2, 3, 4, 5, 6, 7, 8]))

# 3.打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %d' % (j, i, j * i), end="\t")
    print()
# 4.多维数组的展开
# 方法1 使用递归
"""
from collections.abc import *
def flatten(lst, out_lst=None):
    if out_lst is None:
        out_lst = []
    for i in lst:
        if isinstance(i, Iterable): # 判断i是否可迭代
            flatten(i, out_lst) # 尾数递归
        else:
            out_lst.append(i) # 产生结果
    return out_lst
print(flatten([[1,2,3],[4,5]])) # [1, 2, 3, 4, 5]
print(flatten([[1,2,3],[4,5]], [6,7])) # [6, 7, 1, 2, 3, 4, 5]
print(flatten([[[1,2,3],[4,5,6]]])) # [1, 2, 3, 4, 5, 6]
"""
# 方法2:使用numpy
import numpy
b = numpy.array([[1,2,3],[4,5]],dtype=object)
print(b.flatten()) #[list([1, 2, 3]) list([4, 5])]
list1 =[]
for i in b.flatten():
    list1.extend(i)
print('list1=',list1) # list1= [1, 2, 3, 4, 5]
# 5.列表拼接的几种方法
list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2) # [1, 2, 3, 4, 5, 6]
list1.extend(list2)
print(list1) # [1, 2, 3, 4, 5, 6]
# 6.列表等分
from math import ceil
def divide(lst,size):
    if size <= 0:
        return [lst]
    return [lst[i * size:(i + 1) * size] for i in range(0, ceil(len(lst) / size))]
r = divide([1, 3, 5, 7, 9], 2)
print(r) # [[1, 3], [5, 7], [9]]
r = divide([1, 3, 5, 7, 9], 0)
print(r) # [[1, 3, 5, 7, 9]]
r = divide([1, 3, 5, 7, 9], -3)
print(r) # [[1, 3, 5, 7, 9]]
# 7.列表压缩 去除False 元素
print(bool(1)) #True
print(bool(None)) # False
print(bool(0)) # False
print(bool(False)) # False
print(bool('')) # False
def filter_lst(lst):
    return list(filter(bool,lst))
print(filter_lst([1,2,3,None,False,'',0,[1,2]])) # [1, 2, 3, [1, 2]]
# 8.求最大长度的列表
def max_lst(*k):
    return max(*k,lambda x:len(x))
print(max([1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5])) # [1, 2, 3, 4, 5]
# 9.求列表中出现次数最多的元素
def top1(lst):
    return max(lst, default='列表为空', key=lambda v: lst.count(v))
lst = [1, 3, 3, 2, 1, 1, 2]
r = top1(lst)
print(f'{lst}中出现次数最多的元素为:{r}') # [1, 3, 3, 2, 1, 1, 2]中出现次数最多的元素为:1
# 10.求多个列表中的最大值
def max_lists(*lst):
    return max(max(*lst,key=lambda x:max(x)))
print(max_lists([1,2,3],[4,5,6],[10,11,12])) # 12
# 11.判断列表是否有重复元素 使用 set 对列表进行去重处理 然后使用 len()比较列表长度
def has_duplicates(lst):
    return len(lst)==len(set(lst))
print(has_duplicates([1,2,3,4,5])) # True
print(has_duplicates([1,1,2,3,4,2]))  # False

print(list((set([1,2,3,4,1])))) # [1, 2, 3, 4]
# 12.列表反转
def lst_reverse(lst):
    return lst[::-1]
print(lst_reverse([1,2,3,4,5,6,7,8,9])) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
# 13.浮点数等差数列
def rang(start, stop, n):
    start,stop,n = float('%.2f' % start), float('%.2f' % stop),int('%.d' % n)
    step = (stop-start)/n
    lst = [start]
    while n > 0:
        start,n = start+step,n-1
        lst.append(round((start), 2))
    return lst
print(rang(1, 8, 10)) # [1.0, 1.7, 2.4, 3.1, 3.8, 4.5, 5.2, 5.9, 6.6, 7.3, 8.0]
# 14.将列表按照条件进行分组
def sort_lst(lst,f):
    return [[x for x in lst if f(x)],[x for x in lst if not f(x)]]
print(sort_lst([1,2,3,4,5,6,7,8,9,0],lambda x:x>5)) # [[6, 7, 8, 9], [1, 2, 3, 4, 5, 0]]
# 15.列表进行向量运算
def map_lst(*lst):
    return list(map(lambda x,y:x+y,*lst))
print(map_lst([1,2,3],[4,5,6])) # [5, 7, 9]
# 16.返回值最大的字典 items() 返回一个元组对象
dict1 = {"name":'Justin','age':15}
for i in dict1.items():
    print(i)  # ('name', 'Justin') ('age', 15)
def max_pairs(dic):
    if len(dic) == 0:
        return dic
    max_val = max(map(lambda v: v[1], dic.items()))
    return [item for item in dic.items() if item[1] == max_val]
r = max_pairs({'a': -10, 'b': 5, 'c':3,'d':4,'e':6})
print(r)
# 17.合并字典
def merge_dict(list1,list2):
    return {**list1,**list2}
print(merge_dict({'a':1},{'b':2})) # {'a': 1, 'b': 2}
# 18.返回字典的TOPN key
from heapq import nlargest
# 返回字典d前n个最大值对应的键
def topn_dict(d, n):
    return nlargest(n, d, key=lambda k: d[k])
print(topn_dict({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3)) # ['a', 'd', 'c']
# 19.检查两个字符串是否 相同字母异序词，简称：互为变位词
from collections import Counter
def anagram(str1, str2):
    return Counter(str1) == Counter(str2)
print(anagram('eleven+two', 'twelve+one')) # True 这是一对神器的变位词
print(anagram('eleven', 'twelve')) # False
# 20.逻辑上合并字典
dict1 = {'a':1}
dict2 = {'b':2}
dict3 = {**dict1,**dict2} # {'a': 1, 'b': 2}
print(dict3)
dict3['a']=3 # 修改字典的值 不影响原先合并前的字典
print(dict1) #{'a': 1}
print(dict3) # {'a': 3, 'b': 2}
# 使用ChainMap 合并字典，修改字典的值会改变原来的值
from collections import ChainMap
chainDict1 = {'a':1}
chainDict2 = {'b':2}
chainDict3 = ChainMap(chainDict1,chainDict2)
print('chainDict3=',dict(chainDict3)) # chainDict3= {'b': 2, 'a': 1}
print('改变前chainDict1 a 的值',chainDict1['a']) # 改变前chainDict1 a 的值 1
chainDict3['a']=3
print('改变后chainDict1 a 的值',chainDict1['a']) # 改变后chainDict1 a 的值 3
# 21.命名元组提高可用性 使用命名元组写出来的代码可读性更好，尤其处理上百上千个属性时作用更加凸显。
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y', 'z']) # 定义名字为Point的元祖，字段属性有x,y,z
lst = [Point(1.5, 2, 3.0), Point(-0.3, -1.0, 2.1), Point(1.3, 2.8, -2.5)]
print(lst[0].y - lst[1].y) # 3.0
# 22.使用sample 进行样本抽样
from random import randint,sample
lst = [randint(0,50) for _ in range(1,101)]
# 取10个元素
print(lst[1:11]) # [19, 32, 7, 45, 24, 39, 36, 0, 43, 31]
print(sample(lst,10)) # [19, 32, 7, 45, 24, 39, 36, 0, 43, 31]
# 23.使用shuffle对数据集进行重洗
from random import shuffle
list1 = [1,2,3,4,5]
list1.sort(reverse=True) # sort 没有返回值 ，对源列表进行排序
print('排完序后的list1=',list1) # 排完序后的list1= [5, 4, 3, 2, 1]
shuffle(list1) # shuffle()没有返回值
print('shuffle后的list',list1) # shuffle后的list [3, 5, 2, 1, 4]
# 24.10个均匀分布的坐标点
# random模块中的uniform(a,b) 生成[a,b)内的一个随机数，如下生成10个均匀分布的二维坐标点
from random import uniform
uniform = [(uniform(0,10),uniform(0,10)) for _ in range(1,11)]
print(uniform)
# 25.10个高斯分布点
# random模块中的gauss(u,sigma) 生成均值为u, 标准差为sigma的满足高斯分布的值，如下生成
# 10个二维坐标点，样本误差(y-2*x-1)满足均值为0，标准差为1的高斯分布：
from random import gauss
x = range(10)
y = [2*xi+1+gauss(0,1) for xi in x]
points = list(zip(x,y))
print(points)
# 26.chain 高效串联多个容器对象
from itertools import chain
list1 =[1,2,3]
list2 = [4,5,6]
for i in chain(list1,list2):
    print(i)
print("=====================================")
list3 = (7,8,9)
for j in chain(list1,list3):
    print(j)
print("======================================")
dictTest = {'age':18}
for l in chain(list1,dictTest):
    print(l)
# product 案例
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
rtn = product('xyz', '12', repeat=3)
print(list(rtn))


