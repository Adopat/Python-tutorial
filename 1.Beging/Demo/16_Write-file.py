# 创建要写入的文件
filename = "newfile.txt"
myfile = open(filename,'w')
myfile.write("Written with Python\n")
myfile.close()
print("======使用中文写=====")
filename1 = "newfile_zh.txt"
myfile1 = open(filename1,'w',encoding="utf-8")
myfile1.write("这是用中文写的")
myfile1.close()
# 追加文件
print("======追加文件=====")
filename = "newfile.txt"
myfile = open(filename,'a')
myfile.write("Written with Python\n")
myfile.close()
"""
参数总结
r 打开文件以供读取
w 打开文件进行写入(将截断文件)
b 二进制打开
r+ 打开文件进行读写
a+ 打开文件进行读写(追加到结尾)
w+ 打开文件进行读写(截断文件)
"""