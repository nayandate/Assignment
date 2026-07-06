'''
6. Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191

'''

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for i in range(a, b + 1):
    temp = i
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    if rev == i:
print(i)