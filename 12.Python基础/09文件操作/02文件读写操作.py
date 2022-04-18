# 1. read方法
# 1.1. read方法：如果不带任何参数，那么就会把所有内容一次性读取出来
# fp = open("abc.txt","r",encoding='utf-8')
# while True:
#     content = fp.read(2)
#     if content:
#         print(content,end="")
#     else:
#         break
# fp.close()

# 2. readline方法：
# fp = open("abc.txt","r",encoding="utf-8")
# content = fp.readline()
# print(content)
# content = fp.readline()
# print(content)

# 3. readlines方法：
# fp = open("abc.txt","r",encoding="utf-8")
# lines = fp.readlines()
# for line in lines:
#     print(line)
# fp.close()


# 4. 循环文件指针对象：一次性读取一行的数据
# fp = open("abc.txt","r",encoding="utf-8")
# for x in fp:
#     print(x)
# fp.close()

# 5. writelines方法：需要手动的在字符串结尾加上一个换行符，才会换行。否则不会自动换行
fp = open("abc.txt","w",encoding="utf-8")
fp.writelines(["abc\n",'123'])
fp.close()