print("======Question86=====")
'''
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
'''
# print([i for i in [12,24,35,24,88,120,155] if i!=24])
# # 方法二 remove() 只会移除第一个出现的元素
# li = [12, 24, 35, 24, 88, 120, 155]
# li.remove(24)  # this will remove only the first occurrence of 24
# print(li)
print("=====Question87=====")
'''
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
'''
# list1 = [1,3,6,78,35,55]
# list2 = [12,24,35,24,88,120,155]
# print(list(set(list1)& set(list2)))
print("=====Question88=====")
'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
'''
# # 方法一 导致列表顺序改变
# list1 = [12,24,35,24,88,120,155,88,120,155]
# print(list(set(list1)))
# # 方法二 保留原有的列表顺序
# li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# for i in li:
#     if li.count(i) > 1:
#         li.remove(i)
# print(li)
print("=====Question89=====")
'''
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
'''
# class Person:
#     def __init__(self):
#         pass
#     def getGender(self):
#         pass
# class Male(Person):
#     def __init__(self):
#         Person.__init__(self)
#         pass
#     def getGender(self):
#         print("Male")
# class Female(Person):
#     def __init__(self):
#         Person.__init__(self)
#         pass
#     def getGender(self):
#         print("Female")
# male = Male()
# male.getGender()
# female = Female()
# female.getGender()
print("=====Question90=====")
'''
Please write a program which count and print the numbers of each character in a string input by console.
'''
# str = input()
# # for i in str:
# #     print(i)
# # 方法一使用字典推导式+字典便利
# dict = {i:str.count(i) for i in str}
# print(dict)
# for key,value in dict.items():
#     print('{},{}'.format(key,value))
# import string
# # 方法二使用string 模块方法
# s = input()
# for letter in string.ascii_lowercase:
#     cnt = s.count(letter)
#     if cnt > 0:
#         print("{},{}".format(letter, cnt))