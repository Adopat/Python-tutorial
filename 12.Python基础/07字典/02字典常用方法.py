# 1. clear方法：
person = {"username":"zhiliao","age":18}
# print(person)
# person.clear()
# print(person)

# 2. get方法：
# person['username']：如果这个键在字典中不存在，那么就会抛出异常
# person.get("username")：如果这个键在字典中不存在，那么会返回一个None
# username = person['username1']
# username = person.get("username11","abc")
# print(username)


# 3. pop方法：
# del person['username']：这种方式只会直接删除键值对，不会返回任何东西
# person.pop("username")：在删除后会把值返回回来
# value = person.pop("username")
# del person['username']
# print(value)


# 4. popitem方法：
# 随机删除字典中的一个键值对
# person.popitem()
# print(person)


# 5. update方法：
# 在更新的时候，如果键重复了，那么会用新的值覆盖旧的值
# student = {"sno":"1001","class":"python1","username":"abc"}
# student.update(person)
# print(student)

# 6. setdefault方法：
# 如果指定的键在原来字典中存在，那么就会返回这个键的值。如果是不存在，那么就会把这个键值对添加到字典中
value = person.setdefault("username1","abc")
print(value)
print(person)


