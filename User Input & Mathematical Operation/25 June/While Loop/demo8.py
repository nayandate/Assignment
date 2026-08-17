'''
8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4
'''

n1 = int(input("Enter first number = "))
n2 = int(input("Enter second number = "))
count = 0
while n1<=n2:
     if n1==0:
         n1+=5
     elif n1%5==0:
         count+=1
         n1+=5
     else:
         n1=n1+5-n1%5
print("Count = ",count)