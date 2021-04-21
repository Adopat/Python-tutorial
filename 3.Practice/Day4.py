print("=====Question16=====")
'''
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
'''
# lst = [str(i**2) for i in list(map(int,input().split(','))) if i%2!=0]
# print(",".join(lst))
# print("=====Question17=====")
'''
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
'''
# total = 0
# while True:
#     s = input().split()
#     if not s:
#         break
#     cm,num = map(str,s)
#     if cm =="D":
#         total +=int(num)
#     if cm =="w":
#         total -=int(num)
# print(total)
print("=====Question18=====")
'''
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
'''
# import re
# pwd = input().split(',')#ABd1234@1,a F1#,2w3E*,2We3345
# pattern = re.compile(r'[a-z]{1,}')
# pattern1 = re.compile(r'[0-9]{1,}')
# pattern2 = re.compile(r'[A-Z]{1,}')
# pattern3 = re.compile(r'[@#$]')
# for i in pwd:
#     if len(i)>=6 and len(i)<=12 and pattern.findall(i)!=[] and pattern1.findall(i)!=[] and pattern2.findall(i)!=[] and pattern3.findall(i)!=[]:
#         print(i)#ABd1234@1
print("=====Question19=====")
'''
You are required to write a program to sort the (name, age, score) tuples by ascending order 
where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name
2: Then sort based on age
3: Then sort by score
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
'''
# lst = []
# while True:
#     s = input().split(',')
#     if not s[0]:
#         break
#     else:
#         lst.append(tuple(s))
# lst.sort(key=lambda x:(x[0],x[1],x[2]))
# print(lst)#[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
print("=====Question20=====")
'''
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''
class Divisible:
    def by_seven(self,n):
        for i in range(n+1):
            if i % 7 ==0:
                yield i
divisible = Divisible()
generator = divisible.by_seven(int(input("please input a number： ")))
for number in generator:
    print(number)
