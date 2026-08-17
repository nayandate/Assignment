'''
23. Print all characters that occur exactly twice. 
S = "aabbcdee" 
Output: 'a','b','e'
'''

s = input("String: ")

a=""
i=0
while i<len(s):
    if s[i] not in a:
         a+=s[i]
         j = 0
         count=0
         while j<len(s):
             if s[i] == s[j]:
                 count+=1
             j+=1
         if count==2:
             print(s[i],end=" ")
    i+=1