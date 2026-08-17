'''
13. Get the Unicode code point before index.
'''

s = input("Input: ")
n = int(input("Enter index: "))
if len(s)>=n-1:
     print(ord(s[n-1]))
else:
    print("Index out of range.")