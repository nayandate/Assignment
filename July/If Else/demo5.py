'''
5. Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''

password = input("Enter password: ")
length = len(password)
x = 1
digit = 0
sc = 0

if length<=15 and length>=8:
  for ch in password:
    if password[0] <= "Z" and password[0] >= "A":
         if ch == " ":
             x = 0
             break
         if ch == "@" or ch == "#" or ch == "$" or ch == "%" or ch == "&" or ch == "*":
               sc+=1
         if ch <= "9" or ch >= "0":
               digit+=1
else:
   x = 0

if sc>=1 and digit>=2 and x == 1:
     print("Secure Password")
else:
     print("Not Secure Password")
