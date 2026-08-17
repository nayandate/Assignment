'''
8. Toggle the case of each character.
'''

s1 = input("Input: ")
result = ""
i = 0
while i<len(s1):
   if s1[i]>='a' and s1[i]<='z':
         result+=s1[i].upper()
   elif s1[i]>='A' and s1[i]<='Z':
         result+=s1[i].lower()
   i+=1
print("Output",result)