# 1.查看对象是否可以被调用 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
print(callable(str)) # True
print(callable(int)) # True

##但是由于object提供的这个__repr__方法总是返回一个对象， （  类名 + obejct  at + 内存地址  ），
# 这个值并不能真正实现自我描述的功能！！！因此，如果你想在自定义类中实现  “自我描述” 的功能，那么必须重写 __repr__ 方法：
class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id = '+self.id +', name = '+self.name
xiaoming = Student('001','xiaoming')
print(callable(xiaoming)) # False

class Student1():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id = '+self.id +', name = '+self.name
    def __call__(self):
        print('I can be called')
        print(f'my name is {self.name}')
xiaohong = Student1('002','xiaohong')
xiaohong.__call__() #I can be called
                    #my name is xiaohong
# 2.ascii 展示对象
class Student2():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id = '+self.id +', name = '+self.name+"hahhhah"
xiaogang = Student2('003','xiaogang')
print(ascii(xiaogang)) #d = 003, name = xiaoganghahhhah

# 3.ascii 和 str() repr()区别 https://blog.csdn.net/ljr_123/article/details/105141935
# 4.类方法
class Student3():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id = ' + self.id + ', name = ' + self.name + "hahhhah"
    @classmethod
    def f(cls):
        #print("我是类方法！！")
        print(cls)

print(Student3.f()) # <class '__main__.Student3'>

# 5.动态删除属性
delattr(xiaogang,'id')
print(hasattr(xiaogang,'id')) # False

# 6.一键查看对象所有方法 dir()
print(dir(xiaoming))

# 7.动态获取对象属性 getattr()
class Student4():
    def __init__(self,id,name,gender):
        self.id = id
        self.name = name
        self.gender = gender
    def __repr__(self):
        return 'id = ' + self.id + ', name = ' + self.name+ ',gender = ' + self.gender
xiaolan = Student4('004','xiaolan','女')
print(getattr(xiaolan,'id')) # 004
print(getattr(xiaolan,'name')) # xiaolan
print(getattr(xiaolan,'gender')) # 女
print(xiaolan.__repr__()) # id = 004, name = xiaolan,gender = 女
# 8.对象是否有这个属性 hasattr()
print(hasattr(xiaolan,'age')) # False
# 9.返回对象的内存地址 id()
print(id(xiaolan)) # 1770491392448
print(id(xiaogang)) # 1770491392592
# 10. 判断对象是否是类的实例
print(isinstance(xiaolan,Student3)) # False
print(isinstance(xiaolan,Student4)) # True
# 11.父子关系的确定 issubclass()
class Father():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'name =' + self.name + ',age = '+ self.age
class Son(Father):
    def playBall(self):
        pass
print("issubclass的使用")
print(issubclass(Son,Father)) # True
# 12.所有对象的根 object()
o = object()
type(o) # True
# 13.创建属性的两种方式 property() 函数的作用是在新式类中返回属性值。
class C(object):
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self,value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx,setx,delx,"I'm the 'x' property.")
# property() 函数用作装饰器可以很方便的创建只读属性
class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """get the current voltage"""
        return self._voltage

# 14.查看对象的类型 type()
print(type(xiaolan)) # <class '__main__.Student4'>
print(type(Student4)) # <class 'type'>

# 15.元类
print(xiaolan.__class__) # <class '__main__.Student4'>
print(Student4.__class__) # <class '__main__.Student4'>









