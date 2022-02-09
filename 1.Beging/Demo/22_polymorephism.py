# 多态的前提 继承 和方法的重写
# 具有函数的多态
class Bear(object):
    def sound(self):
        print("Groarrr")


class Dog(object):
    def sound(self):
        print("Woof woof!")


def makeSound(animalType):
    animalType.sound()


bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)


# 抽象类的多态
class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Pdf(Document):
    def show(self):
        return "show pdf contents!"


class Word(Document):
    def show(self):
        return "show word contents!"


documents = [Pdf("Document1"), Pdf("Document2"), Word("Document3")]
for document in documents:
    print(document.name + ":" + document.show())
print("=====多态示例=====")


class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Sportscar(Car):
    def drive(self):
        return "Sportscar driving"

    def stop(self):
        return "Sportscar braking"


class Truck(Car):
    def drive(self):
        return "Truck driving slowly because heavily loades."

    def stop(self):
        return "Truck braking!"


cars = [Truck('Bananatruck'),
        Truck('Orangetruck'),
        Sportscar('Z3')]
for car in cars:
    print(car.name + ":" + car.drive())
