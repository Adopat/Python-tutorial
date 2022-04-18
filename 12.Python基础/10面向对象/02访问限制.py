# 1. 受保护的属性或者方法：以_开头的属性或者方法。
# 这类属性或者方法是在语义上不希望被外界调用，但是你一定要调用也是可以的。

# 2. 私有属性或者方法：以两个_开头的属性或者方法。
# 这类属性或者方法外面是不可以进行调用的。

class Person:
    # __init__：构造函数
    def __init__(self,name,age):
        # 定义对象属性
        self._name = name
        self.__age = age

    def greet(self):
        print(f"my name is {self._name},my age is {self.__age}")
if __name__ == '__main__':
    p1 = Person(name="张三",age=18)
    print(p1._name)
    print("年龄：",p1._Person__age)
    # print(p1.__age)
    p1.greet()