# 1. 类方法：
# 1.1. 在方法定义的上面，加上一个@classmethod装饰器，就变成了一个类方法
# 1.2. 类方法的第一个参数，从之前的self变成cls，cls代表的是当前的这个类。
# 1.3. 类方法中，只能通过cls来操作类属性，不能读写实例属性。
# 1.4. 调用类方法，可以有两种方式，第一种方式就通过类名.类方法()，第二种方式是通过对象来调用。
# 1.5. 类方法存在的意义：调用的时候可以直接通过Person.eat()调用，而不需要先创建一个对象再调用。

# 2. 静态方法：
# 1.1. 定义：在函数定义上面，添加一个@staticmethod装饰器，就变成了一个静态方法。
# 1.2. 静态方法在语法上，没有固定的第一个参数。
# 1.3. 静态方法其实就是一个普通的函数，只不过在某些情况下，强制绑定到这个类上。
# 有点类似于工具箱，工具箱中的每个工具（比如螺丝刀）相当于一个函数，都可以单独拿出去用，但是为了方便，我们放到一起，也就是放到类中，以后方便携带和使用。

class Person:
    country = "china"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 装饰器
    @classmethod
    def eat(cls): #cls：class
        # cls == Person
        print(f"我是{cls.country}人")
        print('在吃东西')

    def run(self):
        print('奔跑中')

    @staticmethod
    def show():
        print("我是show方法")

p1 = Person(name="zhiliao",age=18)
Person.eat()
p1.eat()


class MyTool:
    @staticmethod
    def add(a,b):
        return a+b

