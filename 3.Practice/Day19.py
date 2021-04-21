print("=====Question91=====")
'''
Please write a program which accepts a string from console and print it in reverse order.
'''
# print(input()[::-1])
# 方法二
# s = input()
# s = "".join(reversed(s))
# print(s)
print("=====Question92=====")
'''
Please write a program which accepts a string from console and print the characters that have even indexes.
'''
# s = input()#H1e2l3l4o5w6o7r8l9d
# print(s[::2])
# # 方法二
# ns = ""
# for i in range(len(s)):
#     if i % 2 == 0:
#         ns += s[i]
# print(ns)
print("======Question93=====")
'''
Please write a program which prints all permutations of [1,2,3]
'''
# import itertools
# print(list(itertools.permutations([1,2,3])))
print("=====Question94=====")
'''
Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens 
and rabbits in a farm. How many rabbits and how many chickens do we have?
'''
# def f(numhead,numleg):
#     ns ="Not Found"
#     for i in range(numhead+1):
#         j = numhead-i
#         if 2*i + 4*j == numleg:
#             return i,j
#     return ns , ns
# # print(f(35,94))
# print("chickens {} rabbits {}".format(*f(35,94)))
print("=====Question95=====")
'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given scores. Store them in a list and find the score of the runner-up.
'''
arr = map(int,input().split())
arr = list(set(arr))
arr.sort()
print(arr[-2])