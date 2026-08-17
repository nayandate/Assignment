'''
6. Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppecodease letters, lowecodease
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
alphabets and digits - Convert all alphabets to lowecodease - Remove
duplicate alphabets - Arrange alphabets in ascending order - Arrange
digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”

Test Case 1 Input: Enter registration code: zBc@638

Output: Result: bcz863

Test Case 2 Input: Enter registration code: 5Br$dE654b

Output: Result: bder6554

Test Case 3 Input: Enter registration code: A9@C3d#6B1a

Output: Result: abcd9631

Test Case 4 Input: Enter registration code: X#X@M2A4x7

Output: Result: amx742

Test Case 5 Input: Enter registration code: r@T#y

Output: Result: rty No Digits Found
'''

code = input("Enter registration code: ").lower()
digit = ""
alpha = ""
result = ""

i = 0
while i<len(code):
    if (code[i]>="a" and code[i]<="z"):
      if code[i] not in alpha:
         alpha+=code[i]
    elif code[i]>="0" and code[i]<="9":
         digit+=code[i]
    i+=1

j = 97
while j<=122:
   i = 0
   while i<len(alpha):
        if alpha[i] == chr(j):
            result += alpha[i]
        i+=1
   j+=1 

j = 9
while j>=0:
   i = 0
   while i<len(digit):
        if digit[i] == str(j):
            result += digit[i]
        i+=1
   j-=1   

print("Result:",result)
if digit == "":
    print("No Digits Found")