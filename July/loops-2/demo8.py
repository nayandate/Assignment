'''
8. Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
'''
n = int(input("Enter number : "))
no = n
cube = n*n*n
sum = 0
if n<10:
     if cube%10 == n:
         print("Trimorphic Number")
     else:
         print("Not a Trimorphic Number")
else:
     while n>0:
          rem = cube%10
          sum = sum*10+rem
          cube = cube//10
          n = n//10
     n = no
     rev = 0
     while n>0:
          rem = sum%10
          rev = rev*10+rem
          sum = sum//10
          n = n//10

     if no == rev:
         print("Trimorphic Number")
     else:
         print("Not a Trimorphic Number")
