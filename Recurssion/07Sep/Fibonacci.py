'''
Assignment 1: Smart Street Lights (Fibonacci Series)

A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.

Month 1 → 0 lights
Month 2 → 1 light
Every following month, the number of lights installed is the sum of the previous two months.

As a software developer, your task is to help the city planning department generate the installation schedule.

Task

Write a recursive function to print the first N Fibonacci numbers.

Input
Enter the number of months:
7
Output
0 1 1 2 3 5 8
'''

def fibonacci(month):
    if month == 1:
        return 0
    elif month == 2:
        return 1
    return fibonacci(month-1)+fibonacci(month-2)
month = int(input("Enter the number of months: "))
for i in range(month):
    print(fibonacci(i+1),end=" ")