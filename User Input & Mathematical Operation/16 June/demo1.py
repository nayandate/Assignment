'''Assignment 1: Speed Calculator
Write a Python program that:
Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
'''

dist = int(input("Enter Distance : "))
time = int(input("Enter Time : "))
Speed = dist // time 
print("Speed = {} km/h".format(Speed))