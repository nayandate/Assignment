'''
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
'''

pri = int(input("Principal = "))
rate = int(input("Rate = "))
time = int(input("Time = "))

amount = int(pri*(1+rate/100)**time)
CI = int(amount - pri)
print("Amount = ",amount)
print("Compound Interest = ",CI)