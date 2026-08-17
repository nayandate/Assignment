'''
*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3
'''

n = int(input("Number = "))
dig = int(input("Digit = "))
count=0
rem = 0
for i in range (n,0):
    rem = n%10
    if rem == dig:
         count = count+1
    i=n//10
    
print("Digit : ",count)