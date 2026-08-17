'''
12. Get the Unicode code point of a character at index.
'''

s = input("Input: ")
n = int(input("Enter index: "))
if len(s)>n:
     print(ord(s[n]))
else:
    print("Index out of range.")