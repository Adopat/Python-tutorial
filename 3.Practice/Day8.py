print("=====Question36=====")
'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.
'''
# lst = [i**2 for i in range(1,21)][5:]
# print(lst)
print("=====Question37=====")
'''
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included)
'''
# generate_tuple = lambda : (i**2 for i in range(1,21))
# print(*(generate_tuple()))
print("=====Question38=====")
'''
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line
'''
# tuple = tuple((i for i in range(1,11))) # 注意元祖推导式生成并不是一个元组，而是一个迭代对象
# print(tuple)
# print(tuple[:5],tuple[5:])
print("=====Question39=====")
'''
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''
# tuple = tuple((i for i in range(1,11) if i%2==0))
# print(tuple)
print("=====Question40=====")
'''
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
'''
str = input()
if str in ('YES', 'yes', 'Yes'):
    print('YES')
else:
    print('No')
