'''
14. Find the first occurrence of a character.
S = "banana", Char = 'a'
1 (index)
'''

s = input("Input: ")
n = input("Enter char: ")
i = 0
count=0
while len(s)>i:
     if s[i] == n:
          print("Index: ",i)
          break
     else:
          count+=1
     i+=1
if count == len(s):
     print("Character not found")

# print(s.find(n))