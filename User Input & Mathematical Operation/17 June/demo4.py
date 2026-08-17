'''
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
'''


speed = int(input("Enter speed in km/h : "))
hr,min = map(int,input("Enter time (hours and minutes) : ").split())

tt = hr+(min/60)
print(f"Total Time = {tt} hours")

dis = speed*tt
print(f"Speed = {dis} km")

