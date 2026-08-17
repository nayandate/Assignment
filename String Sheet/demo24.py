'''
24. Check if all characters in a string are unique. 
S1 = "abc",  S1: True
S2 = "abca", S2: False
'''

s = input("String: ")
x=0
a=""
i=0
while i<len(s):
      j = 0
      count=0
      while j<len(s):
          if s[i] == s[j]:
              count+=1
          j+=1
      if count!=1:
          x=1
          break
      i+=1
if x==1:
     print("False")
else:
     print("True")