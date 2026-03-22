import math
from tkinter import *
class GeometricObject:
    def __init__(self,filled = False,color = "white"):
        self._filled = filled
        self._color = color

class Triangle(GeometricObject):
    def __init__(self,side1 = 1.0, side2 = 1.0, side3 = 1.0,filled = False,color = "white"):
        super().__init__(color,filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    def get_side1(self):
        return self.__side1
    def get_side2(self):
        return self.__side3
    def get_side3(self):
        return self.__side3
    def getArea(self):
        p = (self.__side1 + self.__side2 + self.__side3) / 2
        S = math.sqrt(p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3))
        return f"Area of triangle: {S}"
    def getPerimeter(self):
        return f"Perimeter of triangle: {self.__side1 + self.__side2 + self.__side3}"
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + ", side2 = " + str(self.__side2) + ", side3 = " + str(self.__side3)

sides = [int(i) for i in input("Enter sides of tringle:").split(' ')]
color = input("Enter the color of triangle:")
indicated = input("Tringle filled or not(1 of 0):")

triangle1 = Triangle(sides[0],sides[1],sides[2])
print(triangle1.getPerimeter())
print(triangle1.getArea())
print("The color of tringle:",color)
print("Tringle filled or no(1 of 0):",indicated)
print()
print()
