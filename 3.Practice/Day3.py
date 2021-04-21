print("=====Question11=====")
'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''
# def check(x):
#     return int(x,2) % 5 ==0
# data = input().split(",")#0100,0011,1010,1001
# data = list(filter(check,data))
# print(",".join(data))#1010
print("=====Question12=====")
'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
# lst = []
# for i in range(1000,3001):
#     flag = 1
#     for j in str(i):
#         if ord(j) % 2 !=0:
#             flag = 0
#     if flag == 1:
#         lst.append(str(i))
# print(",".join(lst))
print("=====Question13=====")
'''
Write a program that accepts a sentence and calculate the number of letters and digits.
'''
# a = input().strip().split()
# number_lst = []
# number_digits = []
# for s1 in a:
#     for s in str(s1):
#         if (ord(s) >= 97 and ord(s) <=122) or (ord(s)>=65 and ord(s)<=90):
#             number_lst.append(s)
#         elif ord(s)>=48 and ord(s)<=57:
#             number_digits.append(s)
#         else:
#             continue
# print("字母个数：",len(number_lst))
# print("数字个数：",len(number_digits))

# 方法二
# word = input()
# letter, digit = 0, 0
# for i in word:
#     print(i)
#     if ("a" <= i and i <= "z") or ("A" <= i and i <= "Z"):
#         letter += 1
#     if "0" <= i and i <= "9":
#         digit += 1
# print("LETTERS {0}\nDIGITS {1}".format(letter, digit))
print("=====Question14=====")
'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
'''
# word = input()
# upper_word = 0
# lower_word = 0
# for i in word:
#     if i.isupper(): #判断是否字符是否小写
#         upper_word +=1
#     elif i.islower():
#         lower_word +=1
#     else:
#         continue
# print(f"UPPER CASE {upper_word}\nLOWER CASE {lower_word}")
print("=====Question15=====")
'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
'''
number = input("please input a number")
print(eval('int(number)+int(number*2)+int(number*3)+int(number*4)'))

