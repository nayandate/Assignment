'''
11. Get the character at a given index.
'''

s = input("Input: ")
n = int(input("Enter index: "))
if len(s)>n:
     print(s[n])
else:
    print("Index out of range.")