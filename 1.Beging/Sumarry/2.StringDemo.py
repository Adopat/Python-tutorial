# 1. 字符串创建
# 2. \转义
# 3. 字符串和数字
print('hello' * 2)  # hellohello
# 4. 字符串打印 f ,format
print("i hava {0} pen,i have {1} apple".format("a", 'ten'))  # # i have a pen ,i have ten aplle
number1 = 'a'
number2 = 'ten'
print(f'i have {number1} pen ,i have {number2} aplle')  # i have a pen ,i have ten aplle
# 5. 字符串常见处理操作
# 5.1 join() 将列表转为字符串
lst = ['hello', 'world', "haha"]
str = ' '.join(lst)
print(str)  # hello world haha
# 5.2 split() 将字符串转为列表
print(str.split())  # ['hello', 'world', 'haha']
# 5.3 split() 指明切割的次数
print(str.split(' ', 1))  # ['hello', 'world haha']
# # 5.4 rsplit() 指明切割的次数 从右边开始切
print(str.rsplit(' ', 1))  # ['hello world', 'haha']
# 5.5 replace startwith,strip() ,lstrip()
# 6. 长字符串切割，借助内置textwrap 模块fill 方法，实现每行指定字符串
import textwrap

words = 'ABCDEFG HIJKLMN OPQ RST UVW XYZ '
r = textwrap.fill(words, 7)
print(r)
# 7.字符串反转
# 字符串反转方法一
print(''.join(reversed("Hello")))  # olleH
# 字符串反转方法二
print("Hello"[::-1])  # olleH
print(list(reversed([1, 2, 3, 4, 5])))  # [5, 4, 3, 2, 1]
# 8.字符串切片
print("Hello"[1:])  # ello
print("Hello"[0:2])  # He
print("Hello"[0:1])  # H
print("Hello"[:])  # Hello 浅拷贝字符串
print("Hello"[0::2])  # Hlo 取奇数位置
print("Hello"[1::2])  # el 取偶数位置
print(len("Hello"))  # 5
# 9.字符串的字节长度 # 一个英文字母占一个字节，中文字符 在UTF-8中 一个中文字符占 3 字节，在gb2312 和 gbk中一个中文占用两个字节
print(len("AAAA".encode('utf-8')))  # 4
print(len("我".encode('utf-8')))  # 3
print(len("我".encode('gb2312')))  # 2
print(len("我".encode('gbk')))  # 2
# Python 正则
