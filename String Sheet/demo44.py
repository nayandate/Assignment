'''
44. Check if two strings are anagrams. 
S1 = "listen", S2 = "silent" 
TRUE
'''

s1 = input("String1: ")
s2 = input("String2: ")
x = 1
i = 0
while i<len(s1):
   ch = s1[i]
   c1 = 0
   c2 = 0
   j = 0
   while j<len(s1):
       if s1[j]==ch:
           c1=c1+1
       j+=1
   j = 0
   while j<len(s2):
       if s2[j]==ch:
           c2=c2+1
       j+=1
   if c1!=c2:
       x=0
       break
   i=i+1
if x==1:
    print("True")
else:
    print("False")