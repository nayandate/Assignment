'''
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''

n = int(input("Enter number = "))
sum=9
while (n>0):
    rem=n%10
    if(rem<=sum):
        sum = rem   
    n=n//10
print("Smallest Digit = ",sum)
          