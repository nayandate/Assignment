'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''

n = int(input("Enter number : "))
sum = 0
mul = 1

while n>0:
     r = n%10
     sum = r+sum
     mul = r*mul
     n = n//10
if sum == mul:
     print("Spy Number")
else:
     print("Not a Spy Number")