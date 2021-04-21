# Python 继承支持多继承
class User:
    name = ""
    def __init__(self,name):
        self.name = name
    def printNmae(self):
        print("Name = "+ self.name)
class Programmer(User):
    def __init__(self,name):
        self.name = name
    def doPython(self):
        print("Programming Python")
brian = User("brain")
brian.printNmae()
print("=====子类调用父类方法=====")
diana = Programmer("Diana")
diana.printNmae() #Name = Diana
diana.doPython() # Programming Python