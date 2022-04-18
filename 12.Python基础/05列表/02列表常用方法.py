# 1. append方法：
# fruits = ['apple','banana']
# fruits.append("orange")
# print(fruits)

# 2. count方法：
# temps = ['to','be','or','not','to','be']
# count = temps.count("be")
# print(count)

# 3. extend方法：会修改原来的列表
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)

# 4. index方法：
# fruits = ['apple','banana']
# index = fruits.index("banana1")
# print(index)

# 5. insert方法：
# fruits = ['apple','banana']
# fruits.insert(1,"orange")
# print(fruits)

# 6. pop方法：栈
# fruits = ['apple','banana']
# item = fruits.pop()
# print(item)
# print(fruits)

# 7. remove方法：
# fruits = ['apple','banana']
# fruits.remove("apple")
# print(fruits)

# 8. reverse方法：会修改原来列表
# 切片逆序不会修改原来列表的值
# numbers = [1,2,3,4,5,6,7,8]
# numbers.reverse()
# print(numbers)
# r_numbers = numbers[-1::-1]
# print(r_numbers)
# print(numbers)

# 9. sort方法：会修改原来列表的值
# sorted函数：不会修改原来列表的值
# numbers = [39,19,402,2,1,56,15]
# numbers.sort(reverse=True)
# print(numbers)
# s_numbers = sorted(numbers)
# print(s_numbers)
# print(numbers)

# 10. del语句：根据下标删除元素
# numbers = [39,19,402,2,1,56,15]
# del numbers[1]
# print(numbers)

# 11. in语法：判断某个元素在列表中是否存在
# numbers = [39,19,402,2,1,56,15]
# if 18 in numbers:
#     print("存在")
# else:
#     print("不存在")

# 12. list函数：将其他的数据类型转换为列表
# 整形、浮点类型、布尔类型这种不是序列的元素不能被强制转换为列表
text = "hello"
# text = 1
result = list(text)
print(result)