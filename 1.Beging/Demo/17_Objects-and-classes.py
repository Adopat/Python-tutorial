# Python 对象
class User:
    name =""
    # __init__() 构造函数
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print("Hello,my name is "+self.name)
# 创建对象
james = User("James")
david = User("David")
eric = User("Eric")
# 调用对象方法
james.sayHello()
david.sayHello()

class CoffeeMachine:
    names = ""
    beans = 0
    water = 0
    def __init__(self,name,beans,water):
        self.name = name
        self.beans = beans
        self.water = water
    def addBean(self):
        self.beans = self.beans + 1
    def removeBean(self):
        self.beans = self.beans - 1
    def addWater(self):
        self.water = self.water + 1
    def removeWater(self):
        self.water = self.water -1
    def printState(self):
        print("Name ="+self.name)
        print("Beans ="+ str(self.beans))
        print("Water ="+str(self.water))
pythonBean = CoffeeMachine("Python Bean",83,20)
pythonBean.printState()
print("=============")
pythonBean.addBean()
pythonBean.printState()