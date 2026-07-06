'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''

n = int(input("enter number = "))
gap = 1
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
        print("Next Prime ID =",num)
        print("Gap =",gap)

        break
    gap+=1
    num+=1