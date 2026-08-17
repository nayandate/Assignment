'''
52. Remove all special characters. 
S = "a!@b#c" 
"abc"
'''

s = input("String: ")
r=""
for i in range(len(s)):
    if s[i] in "!@#$%&":
        r += ''
    else:
        r += s[i]
print(r)