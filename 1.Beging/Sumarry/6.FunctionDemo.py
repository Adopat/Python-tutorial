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
# 4.可变参数
# 5.内置函数
# 6.偏函数 偏函数固定函数的某些参数，重新生成一个新的函数 ，使用partial
from functools import partial
intp = partial(int,base=2)
def init2(s):
    return int(s,base=2) # 注意两种方式的区别
# 7.递归函数
# 8.匿名函数
# 9.高阶函数
# 10.嵌套函数

