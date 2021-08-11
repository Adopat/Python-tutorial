# Tools.py
# 枚举对象 enumerate() 函数用于将一个可遍历的数据对象(如列表,元组或字符串)组合为一个索引序列
# 同时列出数据和数据的下标，一般用在for 循环中
# 使用普通for循环
i = 0
list1=['one','two','three']
for element in list1:
    print(i,element)
    i = i+1
print("=====使用枚举对象 enumerate()=====")
for index,value in enumerate(list1):
    print(index,value)
"""
0 one
1 two
2 three
"""

# 2.查看变量所占的字节数 getsizeof()
import sys
a = 10
b = 10.2
print(sys.getsizeof(a)) # 28
print(sys.getsizeof(b)) # 24
# 可以看到getsizeof()得到的结果并不是和我想象的那样 int 4字节，float4字节，这是因为在Python 中一切都是对象(元类型，深度魔法)，Python中没有明确的数据类型,
# 这里本质上是由python的实现所决定的，python代码在运行的时候会由python解析器执行，具体会解析为C语言的某种结构。也就是说，python中的一个int（或其他）映射到c语言中会是一种复杂结构体。
# （1）sys.getsizeof只计算实际使用的内存大小，引用所消耗的内存大小不计算。
# （2）sys.getsizeof只能作为计算内存大小的参考~
# 3.过滤器filter() 在函数中设定过滤条件
list2 = filter(lambda x:x>10,[x for x in range(1,12)]) # [11]
print(list(list2))
print([x for x in range(1,12) if x>10]) #[11]
# 列表推导式和filter()过滤器性能比较 https://blog.csdn.net/u012424148/article/details/109678431
# 总结 1、推导式可读性比filter加lambda更高，且更简洁。 2、推导式耗时更小。
# 4.返回对象的HASH值 自定义的实例都是可哈希的,list,dict,set等可变对象都是不可哈希的
print(hash(int)) # 8795984118269
#print(hash([1,2,3])) # TypeError: unhashable type: 'list'
# 5.获取帮助 help()
# 6.获取用户输入 input()
# 7.创建迭代器类型 iter() 迭代器适合场景 # https://blog.csdn.net/weixin_38705903/article/details/102870485
# 8.打开文件 open() 一般建议使用上下文管理器 open()
# with open('user.txt') as f:
#     f.read();
# 9.创建range序列 range() 是一个内置函数，用来生成自然数序列
print("=====range=====")
print(range(11))
for i in range(11):
    print(i)
print("====range 步长======")
for i in range(1,11,2):
    print(i)
# 10.列表反转 reverse() reversed() 返回的是一个惰性序列 列表反转的两种方式
print(list(reversed(list(range(1,11))))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(1,11))[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# 11.聚合迭代器
x = ["name","age","gender"]
y =["justin",18,"男"]
list1 = list(zip(x,y))
print(list1)
print(dict(list1)) # {'name': 'justin', 'age': 18, 'gender': '男'}
a = range(5)
b = list('abcde')
print([str(x)+str(y) for x,y in zip(b,a)]) # ['a0', 'b1', 'c2', 'd3', 'e4']
# 12. 链式操作
from operator import add,sub
def add_or_sub(a,b,oper):
    return (add if oper == '+' else sub)(a,b)
print(add_or_sub(1,2,'-'))
# 13.对象序列化，对象序列化，是指将内存中的对象转为可存储或传输的过程，直接一个类对象，传
# 输不方便。
# 但是，当对象序列化后，就会更加方便，因为约定俗成的，接口间的调用或者发起的 web 请
# 求，一般使用 json 串传输。
# 实际使用中，一般对类对象序列化。先创建一个 Student 类型，并创建两个实例。

class Student():
    def __init__(self,**args):
        self.ids = args['ids']
        self.names = args['names']
        self.address = args['address']
xiaoming = Student(ids=1,names='xiaoming',address='北京')
xiaohong = Student(ids=2,names='xiaohong',address='上海')
# 导入json模块，调用dump方法，就会将列表对象 [xiaoming,xiaohong]，序列化到文件 json.txt中。
import json
with open('json.txt','w',encoding='utf-8') as f:
    json.dump([xiaohong,xiaoming],f,default= lambda obj:obj.__dict__,ensure_ascii=False)
