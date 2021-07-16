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
# 0.数据格式是类专有的打印格式
cat = Animal('奔驰',666)
print(cat)
'''
Animal(奔驰,666) is printed
        name =奔驰
        speed =666
'''
# Python 作为动态语言，支持属性的动态添加和删除
cat.color ='red'
print(hasattr(cat,'color')) # True
dog = Animal('宝马',999)
print(dog)
print(hasattr(dog,'color')) # False
# 5.private,protected,public
# self.__speed  (private 属性,属于类)
# self._speed (public 属性，对象可以调用)
# 6.继承 子类继承父类的所有public 和 protected 数据和方法
print("=====继承的使用=====")
class Animal():
    cproup = "我是类的属性cprop"
    def __init__(self,name,speed):
        self.name = name
        self._speed = speed
    def __str__(self):
        return '''Animal({0.name},{0._speed}) is printed
        name={0.name}
        speed={0._speed}'''.format(self)
class Cat(Animal):
    def __init__(self,name,speed,color,genre):
        super().__init__(name,speed)
        self.color = color
        self.genre = genre
jiafeimao = Cat('Coffei',8,'gray','CatGenre')
print(jiafeimao)
'''
Animal(Coffei,8) is printed
        name=Coffei
        speed=8
'''
# 7.多态
print("======不用多态======")
class Animal():
    cproup = "我是类的属性cprop"
    def __init__(self,name,speed):
        self.name = name
        self._speed = speed
    def __str__(self):
        return '''Animal({0.name},{0._speed}) is printed
        name={0.name}
        speed={0._speed}'''.format(self)
class Cat(Animal):
    def __init__(self,name,speed,color,genre):
        super().__init__(name,speed)
        self.color = color
        self.genre = genre
    # 添加方法
    def getRunningSpeed(self):
        print('running speed of %s is %s' % (self.name, self._speed))
        return self._speed
class Bird(Animal):
    def __init__(self,name,speed,color,genre):
        super().__init__(name,speed)
        self.color = color
        self.genre = genre
    # 添加方法
    def getFlyingSpeed(self):
        print('flying speed of %s is %s' % (self.name, self._speed))
        return self._speed
import time
class Manager():
    def __init__(self,animal):
        self.animal = animal
    def recordTime(self):
        self.__t = time.time()
        if isinstance(self.animal, Cat):
            print('feeding time for %s is %.0f'%(self.animal.name,self.__t))
            self.animal.getRunningSpeed()
        if isinstance(self.animal,Bird):
            print('feeding time for %s is %.0f'%(self.animal.name,self.__t))
            self.animal.getFlyingSpeed()
    def getFeedingTime(self):
        return '%0.f'%(self.__t,)

jiafeimao = Cat('Coffei',8,'gray','CatGenre')
cat = Manager(jiafeimao)
cat.recordTime()
'''
feeding time for Coffei is 1626423428
running speed of Coffei is 8
'''
# bird = Bird('Hobby',18,'red','yellow')
# bd = Manager(bird)
# bd.recordTime()
'''
feeding time for Hobby is 1626423519
flying speed of Hobby is 18
'''
print("======不用多态======")
print("=====使用多态，再父类创建一个基类方法=====")
class Animal():
    cprop = "我是类上的属性cproup"
    def __init__(self,name,speed):
        self.name = name
        self._speed = speed
    def __str__(self):
        return '''Animal({0.name},{0._speed}) is printed
        name={0.name}
        speed={0._speed}'''.format(self)
    # 定义一个基类方法
    def getSpeedBehavior(self):
        pass
class Cat(Animal):
    def __init__(self,name,speed,color,genre):
        super().__init__(name,speed)
        self.color = color
        self.genre = genre
    # 重写基类方法
    def getSpeedBehavior(self):
        print('running speed of %s is %s' % (self.name, self._speed))
        return self._speed
class Bird(Animal):
    def __init__(self,name,speed,color,genre):
        super().__init__(name,speed)
        self.color = color
        self.genre = genre
    # 重写基类的方法
    def getSpeedBehavior(self):
        print('flying speed of %s is %s' % (self.name, self._speed))
        return self._speed
import time
class Manager():
    def __init__(self,animal):
        self.animal = animal
    def recordTime(self):
        self.__t = time.time()
        print('feeding time for %s is %.0f' % (self.animal.name, self.__t))
        self.animal.getSpeedBehavior()
    def getFeedingTime(self):
        return "%0.f"%(self.__t,)
print('#'*30)
jiafeimao = Cat('jiafeimao',2,'gray','CatGenre')
haiying = Bird('haiying',40,'red','hhhhh')
Manager(jiafeimao).recordTime()
"""
feeding time for jiafeimao is 1626427190
running speed of jiafeimao is 2
"""
Manager(haiying).recordTime()
"""
feeding time for haiying is 1626427190
flying speed of haiying is 40
"""
print("=====使用多态，再父类创建一个基类方法=====")
# 8.创建抽象方法 借助Python内置的abc 模块，使用abstractmethod装饰器，Animal类的改进版，显示的定义基类的此方法为抽象方法，并且明确指明两个继承类需要重写此方法
import abc
class Animal():
    cprop
