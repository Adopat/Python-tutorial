# 1.类的定义
# 2.实例
# 3.打印实例
# 4.实例属性和类属性
class Animal():
    cprop = "类属性"
    def __init__(self,name,speed): # self 表明此方法是实例上的方法
        self.name = name # self 的作用是指明这两个属性是实例上的，不是类上的
        self.speed = speed
    def __str__(self): # __str__ 魔法函数 打印实例
        return """Animal({0.name},{0.speed}) is printed
        name ={0.name}
        speed ={0.speed}
        """.format(self) # 0.数据名称 类专有的打印格式
# 动态添加属性  hasattr 检测实例是否有某属性
cat = Animal('奔驰',666)
print(cat)
'''
Animal(奔驰,666) is printed
        name =奔驰
        speed =666
'''
cat.color ='red'
print(hasattr(cat,'color')) # True
dog = Animal('宝马',999)
print(dog)
print(hasattr(dog,'color')) # False
# 5.private,protected,public
# 6.继承 子类继承父类的所有public 和 protected 数据和方法
# 7.多态
