print("=====Question81=====")
'''
By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''
# lst = [12,24,35,70,88,120,155]
# lst1 = [i for i in lst if i%5==0 and i%7==0]
# print(lst1)
print("=====Question82=====")
'''
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
'''
# # 方法一
# lst = [12,24,35,70,88,120,155]
# list1 = [i for i in lst if i!=lst[0] and i!=lst[2] and i!=lst[4] and i!=lst[6]]
# print(list1)
# # 方法二
# li = [12, 24, 35, 70, 88, 120, 155]
# li = [li[i] for i in range(len(li)) if i % 2 != 0]
# print(li)
print("=====Question83=====")
'''
By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
'''
# lst = [12,24,35,70,88,120,155]
# list1 = [lst[i] for i in range(len(lst)) if i < 3 or 4 < i]
# print(list1)
print("=====Question84=====")
'''
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
'''
# print([[[0 for i in range(9)] for i in range(5)]for i in range(3)])
print("=====Question85=====")
'''
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''
lst = [12, 24, 35, 70, 88, 120, 155]
list1 = [lst[i] for i in range(len(lst)) if i not in [0, 4, 5]]
print(list1)
