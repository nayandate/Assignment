'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''

n = int(input("enter number = "))
count = 0
for i in range(1,n+1):
    if n%i == 0:
        count+=1          

if count > 2:
    print("Composite Number")
    print("Factors Count =",count)
    for i in range(2,n):
        if n%i == 0:
            print("Smallest Factor =",i)
            break
else:
    print("Not a Composite Number")