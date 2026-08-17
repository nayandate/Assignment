'''
5. Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number
'''

n = int(input("Enter number : "))
sq = n*n
temp = sq
sum = 0
l = len(str(n))
l1 = l
while l>0:
     rem = sq%10
     sum = rem+sum*10
     sq = sq//10
     l = l-1

sum1 = 0
while l1>0:
     rev = sum%10
     sum1 = rev+sum1*10
     sum = sum//10
     l1 = l1-1

if n == sum1:
     print("Automorphic Number")
else:
     print("Not an Automorphic Number")
