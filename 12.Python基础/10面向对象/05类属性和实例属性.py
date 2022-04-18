# 1. 类属性：
# 1.1. 类属性是在类中，直接定义的属性。
# 1.2. 实例属性只能通过对象去调用，不能通过类来调用。
# 1.3. 类属性可以被对象调用。
# 1.4. 如果想要修改类属性，只能通过类型名.类属性的方式修改。

class Person:
    country = "china"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('在吃东西')

    def run(self):
        print('奔跑中')

p1 = Person(name="zhiliao",age=18)
print(Person.country)
print(p1.country)
Person.country = "xxx"
print(Person.country)