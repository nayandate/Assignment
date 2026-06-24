'''
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
'''

a,b,c,d,e = map(int,input("Enter number of marks of 5 subject : ").split())

tl = a+b+c+d+e
print("Total = ",tl)

avr = tl/5
print("Average = ",avr)

print("Percentage = ",avr)
