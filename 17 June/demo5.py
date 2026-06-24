'''
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
'''

ms = int(input("Enter Monthly Salary : "))
wd = int(input("Total working days : "))
wh = int(input("Working hours per day : "))


spd = ms/wd
print("Salary per day = ",spd)

sph = spd/wh
print("Salary per hour = ",sph)