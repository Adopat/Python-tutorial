# 1. 如何定义列表
# 列表是使用中括号来定义的，中间的每个元素是通过英文的逗号来进行分割的
# fruits = ['apple','banana','orange',1]
# print(fruits,type(fruits))

# 2. 列表下标取值
# fruits = ['apple','banana','orange']
# print(fruits[1])

# 3. 遍历列表
# fruits = ['apple','banana','orange']
# for fruit in fruits:
#     print(fruit)

# fruits = ['apple','banana','orange']
# length = len(fruits)
# index = 0
# while index < length:
#     fruit = fruits[index]
#     print(fruit)
#     index += 1

# 4. 列表嵌套
# fruits = ['apple','banana','orange',['dog','cat']]
# for item in fruits:
#     print(item,type(item))

# 5. 列表相加
# fruits = ['apple','banana','orange']
# animals = ['dog','cat']
#
# items = fruits + animals
# print(items)


# 6. 列表切片操作
fruits = ['apple','banana','orange']
fruits[0:2] = ['dog','cat']
print(fruits)

