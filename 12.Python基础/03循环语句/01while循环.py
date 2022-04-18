# 1. while循环的语法：
# index = 1
# while index <= 10:
#     print(index)
#     index += 1


# 2. 求1-100之间的和：
# 1,2.....99,100: 50*101=5050
# num用来保存结果
# index用来保存当前求到几位了
# num = 0
# index = 1
# while index <= 100:
#     num += index
#     index += 1
# print(num)

# 3. 用while打印九九乘法表
# 九九乘法表的规律：
# 1. 总共有9行
# 2. 列数是根据行号来的，在第几行就有几列

# print函数有一个end参数，默认这个参数是\n，也就是换行符
# 如果我们不想要使用默认的换行符，那么可以修改end这个参数为我们想要的字符
# print('hello',end=" ")
# print("world")

row = 1
col = 1
while row <= 9:
    while col <= row:
        print(f"{col}*{row}={row*col}",end=" ")
        col += 1
    row += 1
    col = 1
    print("")






