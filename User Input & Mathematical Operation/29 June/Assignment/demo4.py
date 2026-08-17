'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''
import math
n = int(input("enter number = "))
flag = True

if n < 2:
    print("Not A Prime Number")
    flag = False
else:
    for i in range(2,n):
        if n%i == 0:
            print("Not A Prime Number")
            flag = False
            break
    else:
        print("Prime Number")

if flag:   
    num = n+1
    while True:
        is_prime = True
        if num < 2:
            is_prime = False
        for i in range(2,num//2):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            print("Next Prime =",num)
            break
        num+=1
else:
    num = n-1
    while True:
        is_prime = True
        if num < 2:
            print("Can Not Determine prime")
            is_prime = False
            break
        for i in range(2,num//2):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            print("previous Prime =",num)
            break
        num-=1