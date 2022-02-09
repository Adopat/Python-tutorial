# 封装可以防止意外访问
print("=====私有方法======")


class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print("driving")

    def __updateSoftware(self):
        print("updating software")


redcar = Car()
redcar.drive()
# redcar.__updateSoftware() 外部不能访问类的私有方法
print("=====私有变量=====")


class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print("driving maxspeed " + str(self.__maxspeed))


redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # 并未更改私有变量的值
redcar.drive()
print("=====更改私有变量的值=====")


class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print("driving maxspeed " + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed


redcar = Car()
redcar.drive()
redcar.setMaxSpeed(100)
redcar.drive()
