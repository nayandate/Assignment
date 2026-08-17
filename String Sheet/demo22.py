'''
22. Find the last repeating character. 
S = "abracadabra" 
Output: 'r'
'''

s = input("String: ")
i = len(s)-1
while i>=0:
     count=0
     j = 0
     while j<len(s):
         if s[i]==s[j]:
             count+=1
         j+=1
     if count == 1:
          print("Output:",s[i])
          break
     i -= 1