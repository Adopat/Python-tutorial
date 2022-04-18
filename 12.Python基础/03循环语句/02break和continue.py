
# 1. 跳出当前整个循环
# index = 0
# while index <= 10:
#     print(index)
#     if index == 5:
#         break
#     index += 1

# 2. 猜数字游戏
# number = 65
# while True:
#     value = input("请输入您的数值：")
#     value = int(value)
#     if value == number:
#         print("恭喜！您猜对啦！")
#         break
#     elif value < number:
#         print("您猜小了！")
#     else:
#         print("您猜大了！")


# 3. 跳出当次循环（continue）
# index = 0
# while index <= 9:
#     index += 1
#     if index == 5:
#         continue
#     print(index)



# 4. 打印1-10之间所有的奇数
index = 0
while index <= 9:
    index += 1
    if index % 2 == 0:
        continue
    else:
        print(index)
















