print("=====Question76=====")
'''
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
'''
# 字符串压缩  zlib.compress 压缩 zlib.decompree 解压
# import zlib
# str = b"hello world!hello world!hello world!hello world!"
# z = zlib.compress(str)
# print(zlib.decompress(z).decode("utf-8")) #将byte 对象解码成unicode 编码使用 decode 解码 encode 编码
print("=====Question77=====")
'''
Please write a program to print the running time of execution of "1+1" for 100 times.
'''
# import datetime
# before = datetime.datetime.now()
# for i in range(1,1001):
#     x = 1 + 1
# after = datetime.datetime.now()
# execution_time = after - before
# print(execution_time.microseconds)
# import time
# befor = time.time() #Python time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# for _ in range(100):
#     x = 1 + 1
# after = time.time()
# execution = after - befor
# print(execution)
print("=====Question78=====")
'''
Please write a program to shuffle and print the list [3,6,7,8].
'''
# from random import *
# lst = [3,6,7,8]
# shuffle(lst)
# print(lst)
print("=====Question79=====")
'''
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
'''
# sentence = ['I','You']
# sentence1 = ['Play','Love']
# sentence2 = ['Hockey','Football']
# for i in sentence:
#     for j in sentence1:
#         for k in sentence2:
#             print("{0} {1} {2}".format(i,j,k))
print("=====Question80=====")
'''
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
'''
lst = filter(lambda x: x % 2 != 0, [5, 6, 77, 45, 22, 12, 24])
print(list(lst))
