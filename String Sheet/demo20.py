'''
20. Find the lowest frequency character. 
S = "aabbcde" 
Output: 'c', 'd', 'e' (any one or all)
'''

s = input("String: ")
st=9
i=0
while i<len(s):
    j = 0
    count=0
    while j<len(s):
          if s[i] == s[j]:
               count+=1
          j+=1
    if count<st:
         st=count
         result=s[i]
    i+=1
print("Output:",result)