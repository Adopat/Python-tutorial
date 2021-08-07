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
# 7.创建迭代器类型 iter()