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

