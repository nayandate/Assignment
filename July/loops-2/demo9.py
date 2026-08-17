'''
9. Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
'''

n = int(input("Enter number : "))
fac = 0
i = 1
while i <= n//2:
     if n%i == 0:
         fac = fac+i
     i+=1
if n<fac:
   print("Abundant Number")
else:
   print("Not an Abundant Number")