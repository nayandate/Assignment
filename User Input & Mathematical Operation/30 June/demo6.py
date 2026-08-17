'''
6. Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.
Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.
Input:
24
Output:

Next Prime Cabin = 29
'''

n = int(input("enter number = "))

num = n+1

while True:
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2,num):
        if num%i == 0:
            is_prime = False
            break
    if is_prime:
        print("Next Prime =",num)
        break
    num+=1