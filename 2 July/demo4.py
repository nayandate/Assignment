'''
4. Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''
a = int(input("Enter Your 1st Number: "))
b = int(input("Enter Your 2nd Number: "))

for i in range(a, b + 1):
    sum = 0
    l = len(str(i))
    temp = i

    while temp > 0:
        d = temp % 10
        sum += d ** l
        temp = temp // 10

    if sum == i:
        print(i)