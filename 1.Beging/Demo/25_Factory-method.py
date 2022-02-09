# 工厂方法
class Car(object):
    def factory(type):
        if type == "Rececar":
            return Racecar()
        if type == "Van":
            return Van()

    factory = staticmethod(factory)


class Racecar(Car):
    def drive(self):
        print("Racecar driving.")


class Van(Car):
    def drive(self):
        print("Van driving")


obj = Car.factory("Rececar")
obj.drive()  # Racecar driving.
