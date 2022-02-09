print("=====Question46=====")
'''
Define a class named American and its subclass NewYorker.
'''
# class American:
#     pass
# class NewYorker(American):
#     pass
# american = American()
# newyorker = NewYorker()
# print(american)
# print(newyorker)
print("=====Question47=====")
'''
Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area.
'''
# import math
# class Circle:
#     def __init__(self,r):
#         self.radius = r
#     def area(self):
#         return math.pi *(self.radius**2)
# circle = Circle(5)
# print(circle.area())
print("=====Question48=====")
'''
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
'''
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# rect = Rectangle(6,5)
# print(rect.area())
print("=====Question49=====")
'''
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
'''
# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self,length=0):
#         Shape.__init__(self)
#         self.length = length
#     def area(self):
#         return self.length * self.length
# Asqr = Square(5)
# print(Asqr.area())#25
# print(Square().area())#0
print("=====Question50=====")
'''
Please raise a RuntimeError exception.
'''
raise RuntimeError("something wrong")
