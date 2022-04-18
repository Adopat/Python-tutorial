# 1. for循环基本使用
# name = "zhiliaoketang"
# for char in name:
#     print(char)

# 2. 求1-10之间的和（for循环）
# range(start,end)：是获取[start,end)的数
# result = 0
# for number in range(1,101):
#     result += number
# print(result)

# 3. 求"python papijiang papa mama"中p出现的次数
# text = "python papijiang papa mama"
# count = 0
# for x in text:
#     if x == "p":
#         count += 1
# print(count)

# 4. for循环实现九九乘法表
for row in range(1,10):
    for col in range(1,row+1):
        print(f"{col}*{row}={row*col}",end=" ")
    print("")








