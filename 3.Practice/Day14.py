print("=====Question66=====")
'''
Please write a program which accepts basic mathematic expression from console and print the evaluation result.
'''
# expression = input('please inout mathematic expression:')#5+3
# print(eval(expression))#8
print("=====Question67=====")
'''
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
'''
# def binary(array,target):
#     lower = 0
#     upper = len(array)
#     print("Array Length:",upper)
#     while lower < upper:
#         x = (lower + upper)//2
#         print("Array length",len(array))
#         if target == array[x]:
#             return x
#         elif target < array[x]:
#             upper = x
#         elif target > array[x]:
#             lower = x
# Array = [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99]
# print("The Value Found at Index:", binary(Array, 82))
print("=====Question68=====")
'''
Please generate a random float where the value is between 10 and 100 using Python module.
'''
#生成随机数#
# from random import *
# print(uniform(10,100))
print("=====Question69=====")
'''
Please generate a random float where the value is between 5 and 95 using Python module.
'''
# from random import *
# print(uniform(5,95))
print("=====Question70=====")
'''
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
'''
import random
lst = [i for i in range(0,10,2)]
print(random.choice(lst))