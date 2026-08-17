'''
46. Check if a substring appears at both the start and end. 
S = "abcabca", Sub = "abca" 
TRUE
'''

s = input("String: ")
x=0
sub = input("Substring: ")

count=0
for i in range(len(sub)):
    if s[i] == sub[i]:
         count+=1
if count == len(sub):
     x = 1

count=0
j = 0
for i in range(len(s)-len(sub),   len(s)):
    if s[i] == sub[j]:
         count+=1
    j+=1
if count == len(sub):
     x+=1

if x == 2:
   print("True")
else:
   print("False")

'''
if (a[:len(b)] == b) and ( a[-len(b):] == b):
    print("True")
else:
    print("False")
'''