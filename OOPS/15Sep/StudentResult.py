'''
Assignment 1: Student Result Calculator

A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() - Calculate the total marks.

calculate_percentage() - Calculate the percentage.

display_result() - Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%
'''

class Student:
    def calculate_total(self,eng,maths,sci):
        self.total = eng + maths + sci

    def calculate_percentage(self):
        self.per = self.total/3

    def display_result(self,name,roll):
        self.name = name
        self.roll = roll
        print("Student Name: ",self.name)
        print("Roll Number: ",self.roll)
        print("Total Marks: ",self.total)
        print(f"Percentage: {self.per}%")

s1 = Student()

name = input("Enter Student name: ")
roll = int(input("Enter Roll Number: "))
eng = int(input("Enter English Marks: "))
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))

s1.calculate_total(eng,maths,science)
s1.calculate_percentage()
s1.display_result(name,roll)