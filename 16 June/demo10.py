'''
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
'''

total = int(input("Enter total marks = "))
obt = int(input("Enter obtained marks = "))

per = (obt/total)*100
print(f"Percentage = {per}%")