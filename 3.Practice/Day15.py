print("=====Question71=====")
'''
Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.
'''
# import random
# lst = [i for i in range(10,150) if i%5 ==0 and i%7 ==0]
# print(random.choice(lst))
print("=====Question72=====")
'''
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
'''
# from random import *
# print(sample([i for i in range(100,200)],5))
# print(sample(range(100,200),5))
print("=====Question73=====")
'''
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
'''
# import random
# lst = filter(lambda x: x%2==0,[i for i in range(100,200)])
# print(random.sample(list(lst),5))
print("=====Question74=====")
'''
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
'''
# import random
# lst = [i for i in range(1,1000) if i%5==0 and i%7==0]
# print(random.sample(lst,5))
print("=====Question75=====")
'''
Please write a program to randomly print a integer number between 7 and 15 inclusive.
'''
from random import *
print(randint(7,16))
