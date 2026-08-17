'''
19. Find the highest frequency character. 
S = "abracadabra" 
Output: 'a'
'''

s = input("String: ")
st=0
i=0
while i<len(s):
    j = 0
    count=0
    while j<len(s):
          if s[i] == s[j]:
               count+=1
          j+=1
    if count>st:
         st=count
         result=s[i]
    i+=1
print("Output:",result)