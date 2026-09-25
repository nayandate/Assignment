'''
Assignment 3: Security PIN Verification (Palindrome Number)

A bank allows customers to choose a special PIN. For promotional purposes, the bank rewards customers whose PIN is a palindrome (reads the same from left to right and right to left).

As a software developer, write a recursive program to verify whether the entered PIN is a palindrome.

Task

Write a recursive function to reverse the given number and determine whether it is a palindrome.

Input 1
Enter PIN:
1221
Output 1
Palindrome Number
Input 2
Enter PIN:
1234
Output 2
Not a Palindrome Number
'''

def Palindrome(pin,rev=0):
    if pin == 0:
        return rev
    return Palindrome(pin//10,pin%10+rev*10)
    
PIN = int(input("Enter PIN: "))
rev = Palindrome(PIN)
if rev == PIN:
    print("Palindrome Number..........")
else:
    print("Not a Palindrome Number..........")