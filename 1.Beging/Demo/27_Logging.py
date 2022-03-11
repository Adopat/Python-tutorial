# # Python 日志记录
# print("=====日志示例=====")
# import logging
# logging.warning("This is a warning!")
# print("=====日志严重程度=====")
# import logging
#
# logging.basicConfig(filename='program.log', level=logging.DEBUG)
# logging.warning('An example message.')
# logging.warning('Another message')
# print("=====记录时间=====")
# # import logging
# #
# # logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
# # logging.info('Logging app started')
# # logging.warning('An example logging message.')
# # logging.warning('Another log message')
#
# logging.basicConfig(filename='program1.log', format='%(asctime)s %(message)s', level=logging.INFO)
# logging.info('Logging app started')
# logging.warning('An example logging message.')
# logging.warning('Another log message')


# class Car:
#     # 仅在自己的类或方法（如果已定义）中可访问。 以两个下划线开头
#     __maxspeed = 0
#     __name = ""
#
#     def __init__(self):
#         self.__maxspeed = 200
#         self.__name = "Supercar"
#         self.__updateSoftware()
#
#     def drive(self):
#         print('driving. maxspeed ' + str(self.__maxspeed))
#
#     def setMaxSpeed(self, speed):
#         self.__maxspeed = speed
#
#     def __updateSoftware(self):
#         print('updating software')
#
#
# if __name__ =="__main__":
#     redcar = Car()
#     redcar.drive()
#     redcar.setMaxSpeed(320)
#     redcar.drive()
class Car(object):
    @staticmethod
    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()

    #factory = staticmethod(factory)


class Racecar(Car):
    def drive(self):
        print("Racecar driving.")


class Van(Car):
    def drive(self):
        print("Van driving.")


if __name__ == "__main__":
    # Create object using factory.
    obj = Car.factory("Racecar")
    obj.drive()
    obj2 = Car.factory("Van")
    obj2.drive()
