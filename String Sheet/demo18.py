'''
18. Replace occurrences of a character. 
Input: S = "apple" 
       Old='p'
       New='x' 
Output: "axxle"
'''

s = input("String: ")
old = input("Old: ")
new = input("New: ")
result=""
i=0
while i<len(s):
    if s[i] == old:
         result+=new
    else:
         result+=s[i]
    i+=1
print("Output:",result)
