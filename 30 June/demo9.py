'''
9. Bike Service Kilometer Checker
A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000
'''
n = int(input("enter number = "))
i = 1
service = 3000
while service < n:
    service = 3000*i
    if service > n:
        break
    
    print(service,end=" ")
    i+=1