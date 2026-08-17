'''
3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number
'''

n = int(input("enter number = "))
count = 0
for i in range(2,n):
    if n%i == 0:
        count+=1
        if count >2:
            print("Composite Number")
            break
else:
    print("Not a Composite Number")