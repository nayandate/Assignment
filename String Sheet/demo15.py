'''
15. Find the last occurrence of a character. 
S = "banana", Char = 'a' 
5 (index)
'''

s = input("Input: ")
n = input("Enter char: ")
i = len(s)-1
count=0
while i>=0:
     if s[i] == n:
          print("Index: ",i)
          break
     else:
          count+=1
     i-=1
if count == len(s):
     print("Character not found")

# print(s.rfind(n))