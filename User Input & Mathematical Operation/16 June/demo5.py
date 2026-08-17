'''
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
'''

maths = int(input("Enter the marks of maths : "))
hindi = int(input("Enter the marks of hindi : "))
science = int(input("Enter the marks of science : "))

average = float((maths+hindi+science)/3)
print ("Average = ",average)