print("======Question1=====")
'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
print(*[i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0], sep=",")
print("======Question2======")
'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(8))
print("=====Question3=====")
'''
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
'''
# n = int(input('please input n:\n'))
# dict = {i:i*i for i in range(1,n+1)}
# print(dict) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# print("=====Question4=====")
'''
Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
'''
# a =list(map(int,input().strip().split(',')))
# b = tuple(map(int,input().strip().split(',')))
# print(a)
# print(b)
print("=====Question5=====")
'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''


class StringFun():
    def __init__(self):
        pass

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


str1 = StringFun()
str1.getString()
str1.printString()
