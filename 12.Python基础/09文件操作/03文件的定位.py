# fp.tell()：获取当前文件指针所在的位置，永远都是距离开头的位置

# fp = open("abc.txt","r",encoding='utf-8')
# print(fp.tell())
# fp.read()
# print(fp.tell())

# fp.seek()：设置文件指针的位置
# fp = open("abc.txt","r",encoding='utf-8')
# fp.read(1)
# fp.seek(1,1)
# print(fp.read())

# 设置距离文件末尾3个字符的位置
fp = open("abc.txt","r",encoding='utf-8')
# 先把文件指针设置到末尾
fp.seek(0,2)
fp.seek(fp.tell()-3,0)
print(fp.read())