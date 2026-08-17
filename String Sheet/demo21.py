'''
21. Find the first non-repeating character. 
S = "aabbcde" 
Output: 'c'
'''

s = input("String: ")
i = 0
while i<len(s):
     count=0
     j = 0
     while j<len(s):
         if s[i]==s[j]:
             count+=1
         j+=1
     if count == 1:
          print("Output:",s[i])
          break
     i += 1