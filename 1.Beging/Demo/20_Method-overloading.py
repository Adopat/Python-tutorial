# 方法重载，根据函数定义，可以使用零个，一个，两个或多个参数来调用
class Human:
    def sayHello(self,name = None):
        if name is not None:
            print("hello "+ name )
        else:
            print("hello")
obj = Human()
obj.sayHello()#hello
obj.sayHello("Justin") #hello Justin