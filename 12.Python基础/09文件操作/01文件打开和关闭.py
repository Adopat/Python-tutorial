# 1. 打开文件和关闭
# open函数：第一个参数是文件路径，如果没有写盘符，那么默认就是在当前python所处的文件夹下进行寻找和操作
# File Pointer
# fp = open("abc.txt","w",encoding="utf-8")
# fp.write("hello world")
# fp.close()

# 2. 打开文件的方式：
# 2.1. r(read)：以只读的方式打开
# 2.1.1：r只能用于读，不能用于写。
# 2.2.2：r方式打开文件，如果文件不存在，那么就会报错
# fp = open("abc.txt","r",encoding='utf-8')
# content = fp.read()
# print(content)
# fp.close()

# 2.2. w：以只写的方式打开
# 2.2.1：w只能用于写，不能用于读
# 2.2.2：每次用w打开文件，那么会把原来的内容给清空掉
# fp = open("abc.txt","w",encoding='utf-8')
# fp.write("hello world")
# # content = fp.read()
# fp.close()

# 2.3. a(append)：以追加内容的方式打开
# 2.3.1：a的方式打开文件，不会把原来内容清掉，而是在原来内容后面追加新的内容
# 2.3.2：以a的方式打开的文件，是不能用于读
# fp = open("abc.txt","a",encoding='utf-8')
# # fp.write(",hello zhiliao")
# fp.read()
# fp.close()

# 2.4. rb(read binary)：读取二进制的内容
# 2.5. wb(write binary)：写入二进制的内容
# rb和wb：都不能使用encoding参数，否则会报错
fp1 = open("./images/复联.jpg","rb")
content = fp1.read()

fp2 = open("./images/复联1.jpg","wb")
fp2.write(content)

fp1.close()
fp2.close()