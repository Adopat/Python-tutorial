# 1. 继承
# 1.1. 通过继承，子类可以直接从父类中继承一些属性和方法
# 1.2. 子类在定义类的时候，使用圆括号，圆括号中加上父类的名称就可以继承了
# 1.3. 子类可以添加自己的属性和方法
# 1.4. 可以重写父类的方法。在重写的时候，可以通过super(Student,self).重写的方法名()来调用父类的方法，如果不需要执行父类的代码，那就不需要写super。一旦重写了，以后子类调用这个方法的时候，就直接执行子类的这个方法。
# 1.5. 子类不能继承父类的私有属性和方法。
# 1.6. 多继承中，走的是广度优先，可以通过类名.__mro__来获取执行顺序

# Person：相对于Student来讲，是父类
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__idcard = "xxx"

    def eat(self):
        print('在吃东西')

    def run(self):
        print('奔跑中')


# Student：相对于Person来说，是子类
class Student(Person):
    def __init__(self,name,age,school):
        # 调用父类的函数
        super(Student, self).__init__(name,age)
        self.school = school

    def eat(self):
        super(Student,self).eat()
        print("我是学生，我在吃东西")

    def study(self):
        print("正在学习...")


# s1 = Student(name="zhiliao",age=18,school="清华大学")
# s1.eat()
# s1.study()
# print(s1.name)


class Animal(object):
    def eat(self):
        print('动物吃东西')

class Ma(Animal):
    def qima(self):
        print('骑马')

    def eat(self):
        print('马吃草')
        super(Ma,self).eat()
        print('马吃完了草')

class Lv(Animal):
    def lamo(self):
        print('驴拉磨')

    def eat(self):
        print('驴吃麦子皮')
        super(Lv,self).eat()
        print('驴吃完了麦子皮')

class Luozi(Ma,Lv):
    def eat(self):
        super(Luozi,self).eat()
        print('骡子既吃草又吃麦子皮')


luozi = Luozi()
luozi.eat()
print(Luozi.__mro__)