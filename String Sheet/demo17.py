'''
17. Remove occurrences of a character. 
S = "banana", Char = 'a', 
Remove All "bnn"
'''

s = input("String: ")
char = input("Char: ")
result=""
i=0
while i<len(s):
    if s[i] != char:
         result+=s[i]
    i+=1
print("Output:",result)