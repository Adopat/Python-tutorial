# print("======Question56=====")
# print(u'hello world')# u''后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
# print("=====Question57=====")
'''
Write a program to read an ASCII string 
and to convert it to a unicode string encoded by utf-8.
'''
# s = input() #49
# u = s.encode("utf-8")
# print(u) # b'49'
print("=====Question58=====")
'''
Write a special comment to indicate a Python source code file is in unicode.
'''
# -*- coding: utf-8 -*-
print("=====Question59=====")
'''
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
'''
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i/(i+1)
# print("sum =",round(sum,2))
print("=====Question60=====")
'''
Write a program to compute:
𝑓(𝑛)=𝑓(𝑛−1)+100
f(n)=f(n−1)+100
when n>0
and 
𝑓(0)=0
f(0)=0
with a given n input by console (n>0).
'''


def f(n):
    if n == 0:
        return 0
    else:
        return f(n - 1) + 100


print(f(5))
