print("=====Question96=====")
'''
You are given a string S and width W. 
Your task is to wrap the string into a paragraph of width.
'''
import textwrap
# def wrap(string,max_width):
#     string = textwrap.wrap(string,max_width)
#     string = " ".join(string)
#     return string
# if __name__ == "__main__":
#     string,max_width = input().strip().split()
#     result = wrap(string, int(max_width))
#     print(result)
# 方法二
# import textwrap
#
# string = input()
# width = int(input())
# result =textwrap.fill(string, width)
# print(" ".join(result.split("\n")))
print("======Question97=====")
'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
'''
print("=====Question98=====")
'''
You are given a date. Your task is to find what the day is on that date.
'''
# import calendar
# month,day,year = map(int,input().split())#04 16 2021
# dayId = calendar.weekday(year,month,day)
# print(calendar.day_name[dayId].upper())#FRIDAY
print("=====Question99=====")
'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
# 异或
'''
n = int(input())#5
set1 = set(map(int, input().split()))#1 2 3 4 5

m = int(input())#5
set2 = set(map(int, input().split()))#5 6 7 8 9

ans = list(set1 ^ set2)
ans.sort()
for i in ans:
    print(i,end=" ")# 1 2 3 4 6 7 8 9


