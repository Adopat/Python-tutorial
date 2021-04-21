# 递归 ，如果函数调用自身并且具有终止条件
print("=====for循环=====")
def sum(list):
    sum = 0
    for i in range(0,len(list)):
        sum = sum + list[i]
    return sum
print(sum([5,7,3,8,10]))
print("=====递归=====")
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])
print(sum([5,7,3,8,10]))
print("=====递归阶乘=====")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
print("=====递归限制=====")
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3000))
print("=====修改递归调用的数量=====")
import sys
sys.setrecursionlimit(5000)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(1000))