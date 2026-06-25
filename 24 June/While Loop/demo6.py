'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
'''

n = int(input("Number = "))
temp = n
no=0
rev=0
while(n>0):
    rev=n%10
    no = rev*rev*rev+no
    n=n//10
if no == temp:
    print("Armstrong number ")
else:
    print("Not armstrong number ")