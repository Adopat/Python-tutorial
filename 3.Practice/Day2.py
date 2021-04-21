print("=====Question6=====")
'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:
'''
# from math import sqrt
# C , H = 50,30
# def calc(D):
#     return sqrt((2 * C * D) / H)
# D = list(map(int,input().strip().split()))
# D = list(map(calc,D))
# print(D)
print("=====Question7=====")
'''
_Write a program which takes 2 digits, X,Y as input and generates 
a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i _ j.*
'''
# x , y = map(int,input().split(','))
# lst = [[i*j for j in range(y)] for i in range(x)]
# print(lst)
print("=====Question8=====")
'''
Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them alphabetically.
'''
# a = input().split(',') #without,hello,bag,world
# a.sort()
# print(','.join(a))
print("=====Question9=====")
'''
Write a program that accepts sequence of lines as input 
and prints the lines after making all characters in the sentence capitalized.
'''
# def user_input():
#     while True:
#         s = input()
#         if not s:
#             return
#         yield s
# for line in map(str.upper,user_input()):
#     print(line)
print("=====Question10=====")
'''
Write a program that accepts a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words and sorting them alphanumerically.
'''
sequence = input().strip().split()
for s in sequence:
    if sequence.count(s) > 1:
        sequence.remove(s)
print("排序前：",sequence)
sequence.sort()
print("去除重复值排序后的结果："," ".join(sequence))