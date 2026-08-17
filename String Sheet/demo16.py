'''
16. Count total occurrences of a character. 
S = "programming", Char = 'g' 
2
'''

s = input("Input: ")
n = input("Enter char: ")
count = 0
i = 0
while i<len(s):
     if s[i] == n:
         count+=1
     i+=1
print("Count =",count)