aTuple = ('apple','banana','orange')

# 1. 元组取值，通过下标
# aTuple = ('apple','banana','orange')
# print(aTuple[1])

# 2. 循环元组，也是使用for循环更合适
# for item in aTuple:
#     print(item)

# 3. 切片操作：
# print(aTuple[0:2])

# 4. 解组：
# 在解组的时候，如果某个变量不想要，那么可以使用_来代替，并且一定要保证解组的变量个数必须和元组个数一致
person = ("zhiliao",18,"湖南")
# name,age,city = person
name,age,_ = person
print(name,age)