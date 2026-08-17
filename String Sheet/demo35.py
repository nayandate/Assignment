'''
35. Find the first palindrome word. 
S = "this madam is here" 
"madam"
'''

s = input("Input: ")
spl = s.split()
i=0
while i<len(spl):
     result=spl[i][::-1]
     if spl[i].upper() == result.upper():
         print(spl[i])
         break
     i+=1