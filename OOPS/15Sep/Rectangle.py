'''
Assignment 4: Rectangle Calculator

A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:

Length

Breadth

Create the following methods:

calculate_area() - Calculate the area.

calculate_perimeter() - Calculate the perimeter.

display_result() - Display length, breadth, area, and perimeter.

Formulas:

Area = Length * Breadth
Perimeter = 2 * (Length + Breadth)

Sample data:

Length: 15
Breadth: 8
'''

class Rectangle:
    def calculate_area(self,length,breadth):
        self.length = length
        self.breadth = breadth
        self.area = self.length * self.breadth

    def calculate_perimeter(self):
        self.per = 2 * (self.length + self.breadth)

    def display_result(self):
        print()
        print("Length : ",self.length)
        print("Breadth : ",self.breadth)
        print("Area : ",self.area)
        print("Perimeter : ",self.per)

s1 = Rectangle()
len = int(input("Enter length: "))
bre = int(input("Enter breadth: "))

s1.calculate_area(len,bre)
s1.calculate_perimeter()
s1.display_result()