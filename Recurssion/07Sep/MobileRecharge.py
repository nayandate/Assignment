'''
6. Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number
'''

def prime(num,i=2):
    if i == num//2:
        return 
    if num%i==0:
        return False
    return prime(num,i=i+1)
num = int(input("Enter Coupon Number: "))
prime(num)
if prime(num,i=2) == False:
    print("Not Prime Number")
else:
    print("Prime Number")
