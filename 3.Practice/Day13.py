print("=====Question61=====")
'''
The Fibonacci Sequence is computed based on the following formula:
f(n) == 0 if n==0
f(n) ==1 if n==1
f(n) = f(n-1) + f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
'''
# def f(n):
#     if n == 1:
#         return 1
#     elif n ==0:
#         return 0
#     else:
#         return f(n-1) + f(n-2)
# n = int(input("please input a number:\n"))
# print(f(n))
print("=====Question62=====")
'''
The Fibonacci Sequence is computed based on the following formula:
f(n) == 0 if n==0
f(n) ==1 if n==1
f(n) = f(n-1) + f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
'''
# def f(n):
#     if n <2:
#         fibo[n] = n
#         return fibo[n]
#     fibo[n] = f(n-1) + f(n-2)
#     return fibo[n]
# n = int(input())
# fibo = [0] * (n+1)
# f(n)
# fibo = [str(i) for i in fibo]
# ans = ",".join(fibo)
# print(ans)
print("=====Question63=====")
'''
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
'''
# n = int(input("please input a number:\n"))
# lst = map(str,[i for i in range(n+1) if i%2==0])
# print(",".join(list(lst)))
print("=====Question64=====")
'''
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
'''
# n = int(input("please input a number:\n"))
# lst = map(str,list(filter(lambda x : x %5==0 and x%7==0,[i for i in range(n+1)])))
# print(",".join(list(lst)))
print("=====Question65=====")
'''
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
'''
data = [2, 4, 5, 6]
for i in data:
    assert i % 2 == 0, "{0} is not an even number".format(i)
