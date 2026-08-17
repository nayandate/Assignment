'''
5. Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''

code = input("Enter product code: ").lower()
length = len(code)
i = 0
x = 0
while (i<length//2):
      z = length -1 - i
      if code[i] != code[z]:
           x = 1
           break
      i+=1
if x == 1:
    print("Not a Palindrome Code")
else:
    print("Palindrome Code")