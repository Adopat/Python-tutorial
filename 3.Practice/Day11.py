print("=====Question51=====")
'''
Write a function to compute 5/0 and use try/except to catch the exceptions.
'''
# def division():
#     return 5/0
# try:
#     division()
# except ZeroDivisionError as ze:
#     print("除数不能为0")
# except:
#     print("未知错误")
print("=====Question52=====")
'''
Define a custom exception class which takes a string message as attribute.
'''
# class CustomException(Exception):
#     """
#     Exception raised for custom purpose
#     Attribute:
#         message --explaination of the error
#     """
#     def __init__(self,message):
#         self.message = message
# num = int(input())
# try:
#     if num <10:
#         raise CustomException("Input is less than 10")
#     elif num>10:
#         raise CustomException("Input is grater than 10")
# except CustomException as ce:
#     print("The error raised :"+ ce.message)
print("=====Question53=====")
'''
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address. 
Both user names and company names are composed of letters only.
'''
# import re
# email = 'john@google.com'
# pattern = "(\w+)@\w+.com"
# ans = re.findall(pattern,email)
# print(ans)
print("=====Question54=====")
'''
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the company name of a given email address. 
Both user names and company names are composed of letters only.
'''
# import re
# email = 'john@google.com'
# pattern = r"\w+@(\w+).com"
# ans = re.findall(pattern,email)
# print(ans)
print("=====Question55=====")
'''
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
'''
import re

email = input()  # justin 123 qq.com1 999
pattern = r"\d+"
ans = re.findall(pattern, email)
print(ans)  # ['123', '1', '999']
