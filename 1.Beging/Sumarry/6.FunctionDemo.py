# 1. 函数定义
# 2. 引用传参
def foo(nums):
    """
    :param nums:
    :return: 偶数序列
    """
    lst = []
    for num in nums:
        if num % 2 == 0:
            lst.append(num)
    return lst
print(foo([1,2,3,4,5])) # [1,2,3,4,5] 实参 nums 形参
# 3. 默认参数与关键字参数
def foo(length,width,height=1.0): # height 为默认参数
    pass
foo(width=2.0,length=1.0)# 确定这种调用后width 和 length 才是关键字参数
# 4.可变参数 Java 和C++使用函数重载的方式，解决参数个数不同，Python使用可变参数的方法,带*号参数实际被解释为元组对象
print("======可变参数指的是形参前带有*的变量=====")
def foo(length,*others):
    s = length
    for para in others:
        s *=para
    return s
print(foo(5,4,3,2,1))
print(foo(2,5,6))
# 5.内置函数
print("=====内置函数=====")
# pow() 幂次函数
print(pow(2,3))#8
print(pow(4,0.5))#2.0
# max,min
# sorted sorted 函数完成对对象排序，他能接受一个指定排序规则的函数
d = {'a':0,'b':-2,'c':1}
print(d.items())#dict_items([('a', 0), ('b', -2), ('c', 1)])
# 按照values绝对值进行升序
dr = sorted(d.items(),key=lambda x:abs(x[1]))
print(dr)#[('a', 0), ('c', 1), ('b', -2)]
# 6.偏函数 偏函数固定函数的某些参数，重新生成一个新的函数 ，使用partial,要修改内置函数的默认参数可以使用偏函数
from functools import partial
intp = partial(int,base=2)
def init2(s):
    return int(s,base=2) # 注意两种方式的区别
# 7.递归函数 递归函数是值调用自身的函数,使用递归反转字符串
print("=====递归函数=====")
def reverseStr(s):
    if not s:
        return s
    return reverseStr(s[1:])+s[0]
print(reverseStr('ABCDEFG'))#GFEDCBA
# 8.匿名函数 #匿名函数是值使用lambda关键字创建的函数
def f(x,y):
    return x*y
print("=====使用匿名函数=====")
lambda x,y:x*y
# 9.高阶函数 可以用来接受另一个函数作为参数的函数叫做高阶函数
print("=====使用高阶函数=====")
# map()
m = map(lambda s: s.capitalize(),['python','java','C'])
print(list(m))#['Python', 'Java', 'C']
# reduce() 使用reduce 求列表和
from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))#15
# 10.嵌套函数 嵌套函数是指函数里面再套函数的函数,使用嵌套函数的场景，实现某一功能只需要编写2个函数，写成class没有必要
# 写成嵌套后某些参数可以共享，亲和性会更好
def outer():
    name ="Python"
    def inner():
        print(name)
    return inner()
outer()#Python
# 函数闭包 在一些语言中，在函数中可以（嵌套）定义另一个函数时，如果内部的函数引用了外部的函数的变量，则可能产生闭包。闭包可以用来在一个函数与一组“私有”变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能够保持其持久性。
print("=====使用__closure__判断函数是不是闭包")
def outer():
    name ="Python"
    def inner():
        print(name)
    print(inner.__closure__)
    return inner()
outer()#(<cell at 0x000001FE2A597880: function object at 0x000001FE2A59B280>, <cell at 0x000001FE2A597850: str object at 0x000001FE2A2C6E30>)
# 函数不是闭包的情况输出None
print("函数不是闭包的情况")
name ="Python"
def outer():
    def inner():
        print(name)
    print(inner.__closure__)
    return inner()
outer()


