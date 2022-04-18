# 1. 字典的定义
# person = {'username':"zhliao","age":18}
# person = dict(username="zhiliao",age=18)
# print(person,type(person))

person = {'username':"zhliao","age":18}

# 2. 获取字典元素个数：键值对
# person = {'username':"zhliao","age":18}
# print(len(person))

# 3. 通过key获取value
# username = person["username"]
# print(username)

# 4. 给指定的key赋值：
# person['username'] = "hello"
# print(person)

# 5. 删除键值对
# del person['age']
# print(person)

# 6. in判断某个键是否在字典中：
# if "username1" in person:
#     print(person['username'])
# else:
#     print("这个键值对不存在！")

test = {[1,2]:"xxx"}
print(test)