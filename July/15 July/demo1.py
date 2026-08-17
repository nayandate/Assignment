'''
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012
'''

acc = input("Enter account number: ")
length =("*")*(len(acc)-4)

for ch in acc:
     if ch>="0" and ch<="9":
         x = 1
     else:
         x = 0
         break
if x == 1:
    print(length,end="")
    print(acc[-4:],end="")
else:
    print("Invalid Input")