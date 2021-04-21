print("=====Question21=====")
'''
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
# import math
# lst = [0,0]
# while True:
#     s = input().split()
#     if not s:
#         break
#     directions = s[0]
#     distance = s[1]
#     if directions == 'UP':
#         lst[0] += int(distance)
#     elif directions == 'DOWN':
#         lst[0] -= int(distance)
#     elif directions == 'LEFT':
#         lst[1] -= int(distance)
#     elif directions == 'RIGHT':
#         lst[1] += int(distance)
# print(round(math.sqrt(lst[0]**2+lst[1]**2)))
print("=====Question22=====")
'''
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically.
'''
# 方法一：使用pprint 的排序功能
# from pprint import pprint
# p = input().split()
# for i in p:
#     print(i)
# pprint({i: p.count(i) for i in p})
# 方法二：使用 sorted()排序，任何可迭代对象都可以使用sorted
# p = input().split()
# word = sorted(set(p))
# for i in word:
#     print("{0}:{1}".format(i,p.count(i)))
print("=====Question23=====")
'''
Write a method which can calculate square value of number
'''
# def square(x):
#     return x**2
# print(square(5))
# print("=====Question24=====")
# print(str.__doc__)
# print(sorted.__doc__)
# def square(x):
#     """
#
#     :param x:
#     :return: x**2
#     """
#     return x**2
# print(square.__doc__)
print("=====Question25=====")
class Car:
    name = "Car"
    def __init__(self,name=None):
        self.name = name
honda = Car("honda")
print(f'{Car.name} name is {honda.name}')
toyota = Car()
print(f'{Car.name} name is {toyota.name}')
bentian = Car()
bentian.name = "bentian"
print(f'{Car.name} name is {bentian.name}')
