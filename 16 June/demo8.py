'''
Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
'''

mb = int(input("MB = "))
gb = float(mb/1024)
print("GB = ",gb)