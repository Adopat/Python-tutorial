# 1. 字符串创建
# 2. \转义
# 3. 字符串和数字
print('hello'*2) # hellohello
# 4. 字符串打印 f ,format
print("i hava {0} pen,i have {1} apple".format("a",'ten')) # # i have a pen ,i have ten aplle
number1 = 'a'
number2 = 'ten'
print(f'i have {number1} pen ,i have {number2} aplle') # i have a pen ,i have ten aplle
# 5. 字符串常见处理操作
# 5.1 join() 将列表转为字符串
lst = ['hello','world',"haha"]
str = ' '.join(lst)
print(str) # hello world haha
# 5.2 split() 将字符串转为列表
print(str.split()) # ['hello', 'world', 'haha']
# 5.3 split() 指明切割的次数
print(str.split(' ',1)) #['hello', 'world haha']
# # 5.4 rsplit() 指明切割的次数 从右边开始切
print(str.rsplit(' ',1)) # ['hello world', 'haha']
# 5.5 replace startwith,strip() ,lstrip()
# 6. 长字符串切割，借助内置textwrap 模块fill 方法，实现每行指定字符串
import textwrap
words ='ABCDEFG HIJKLMN OPQ RST UVW XYZ '
r = textwrap.fill(words,7)
print(r)