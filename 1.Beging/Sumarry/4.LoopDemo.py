# 1. if 语句
# 2. for 控制循环次数，迭代容器中的元素
# 3. while,break,continue
# 4. for 使用注意，for 语句遍历容器类型或可迭代类型时，如果涉及到增加，删除元素，就需要小心
def delItem(lst,target):
    for item in lst:
        if item == target:
            lst.remove(item)
    return lst
newList = delItem([1,2,3,4,5,1,1,1,1,9],1)
print('删除后的list:',newList) # [2, 3, 4, 5, 1, 1, 9] 可以看到还是有重复数据未删除,列表或数组删除元素时，其后面的元素都会逐次前移1位，但是for 依然会正常迭代，因此“成功”规避了相邻的后面元素1.

def delItem1(lst,target):
    i = 0
    while i<len(lst):
        if lst[i] == target:
            del lst[i]
            i -=1
        i +=1
    return lst
newList1 = delItem1([1,2,3,4,5,1,1,1,1,9],1)
print('删除后的list:',newList1) # 删除后的list [2, 3, 4, 5, 9]

# 5. range()
print(type(range(10)))
from collections.abc import Iterable
print(isinstance(range(10),Iterable)) # True
# range() 函数为了高效节省内存，一次只返回一个值，而不是直接将构成序列的全部元素加载到内存中
# # range() 不支持创建浮点序列
# print(list(range(0,10,0.2))) # TypeError: 'float' object cannot be interpreted as an integer
# 定义一个返回浮点序列
def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i += step
fr = frange(0,1.,0.2) # [0, 0.2, 0.4, 0.6000000000000001, 0.8]
print(list(fr))
# 6. Python 的特色 找出2到15的所有素数,如果不是素数打印出一对因子
for num in range(2,16):
    is_prime = True
    for item in range(2,num):
        if num % item == 0:
            print('%d = %d *%d'%(num,item,num//item))
            is_prime = False
            break
    if is_prime:
        print("%d is prime" % (num))
# 使用 for else 简化代码
print("====== for else ===== ")
# for 遍历完成后执行else,但是触发break 后，else不执行
for num in range(2,16):
    for item in range(2,num):
        if num % item == 0:
            print('%d = %d *%d' % (num, item, num // item))
            break
    else:
        print("%d is prime" % (num))
# try except else try 保护的代码通过后，else才执行，放到else 中的代码，意味着这块代码不必受保护
# while True:
#     try:
#         a = int(input("please input a number:"))
#     except ValueError:
#         print('input value is not a valid number')
#     else:
#         if a%2 == 0:
#             print('{} 是偶数'.format(a))
#         else:
#             print('{} 是一个奇数'.format(a))
# pass 关键字，放在类或函数中，表示类和函数暂不定义
print("=====pass有用的用法=====")
from interface import implements,Interface
class MyInterface(Interface):
    def method1(self,x):
        pass
    def method2(self,x,y):
        pass
class MyClass(implements(MyInterface)):
    def method1(self,x):
        return x *2
    def method2(self,x,y):
        return x + y
# return 和 yield 关键字
'''
共同点：程序遇到return 和 yield 都是立即中断返回
不同点：
    return：中断后，return 下一次执行还是从函数体的第一句执行
    yield: yield 中断返回后，下一次迭代会进入到yield 后面下一行的代码
'''
print('======yield 的用法=====')
def fibonacci(n):
    a , b = 1, 1
    for _ in range(n):
        yield a
        a ,b = b, a+b
for fib in fibonacci(10):
    print(fib)


