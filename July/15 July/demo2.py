'''
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST

'''

name = input("Enter employee name: ").upper()

if name[0]<='Z' and name[0]>='A':
     result = name[0]
else:
     result = ""
i = 0
while i<len(name):
      if name[i]>="A" and name[i]<="Z":
          if name[i-1] == " ":
             result=result+name[i]
      i+=1
if result == "":
    print("Invalid Input:")
else:
    print("Employee Short ID:",result)