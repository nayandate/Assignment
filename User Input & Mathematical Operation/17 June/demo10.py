'''
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
'''

ts = int(input("Enter total seconds : "))

hours = ts//3600
print("Hours = ",hours)

mins = (ts%3600)//60
print("Minutes = ",mins)

sec = ts%60
print("Seconds = ",sec)