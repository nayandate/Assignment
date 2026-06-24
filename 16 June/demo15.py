'''
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
'''

dis1 = int(input("Distance1 = "))
time1 = int(input("Time1 = "))
dis2 = int(input("Distance2 = "))
time2 = int(input("Time2 = "))

dis = dis1 + dis2
time = time1 + time2
aver = dis/time
print(f"Average Speed = {aver} km/h")