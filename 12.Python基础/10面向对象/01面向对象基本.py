# 1. 定义类
# 1.1. 类名习惯用大驼峰命名法
# 1.2. 类中的方法第一个参数都是为self，这个self代表的是，以后用这个类创建的某个对象
# 1.3. __init__是构造函数，每个类都有这个方法。用来给对象进行初始化的。
class Person:
    # __init__：构造函数
    def __init__(self,name,age):
        # 定义对象属性
        self.name = name
        self.age = age

    def greet(self):
        print(f"my name is {self.name},my age is {self.age}")

# 2. 使用类创建对象
# 使用Person创建对象的时候，__init__需要传什么参数，那么Person上面也要传什么参数
zhangsan = Person(name="张三",age=18)
zhangsan.greet()

lisi = Person(name="李四",age=20)
lisi.greet()