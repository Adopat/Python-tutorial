print("=====Question41=====")
'''
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
'''
# lst = map(lambda x:x**2,[i for i in range(1,11)])
# print(list(lst))
print("=====Question42=====")
'''
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''
# lst = map(lambda x:x**2,list(filter(lambda x: x%2==0,[i for i in range(1,11)])))
# print(list(lst))
print("=====Question43=====")
'''
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
'''
# lst = filter(lambda x:x%2==0,[i for i in range(1,21)])
# print(list(lst))
print("=====Question44=====")
'''
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
'''
# lst = map(lambda x:x**2,[i for i in range(1,21)])
# print(list(lst))
print("=====Question45=====")
'''
Define a class named American which has a static method called printNationality.
静态方法
注意静态方法和类方法的区别，两者都可以直接被类调用，类方法有参数cls,静态方法不存在参数
'''
class American:
    # def __init__(self):
    #     pass
    @staticmethod
    def printNationality():
        print("I am a American")

american = American()
american.printNationality() # 如果没有@staticmethod 修饰这个方法不会运行
American.printNationality()