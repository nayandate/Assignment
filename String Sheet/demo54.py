'''
54. Replace duplicate chars with '$'. 
S = "hello" 
"he$lo"
'''

s = input("String: ")
r=""
for i in range(len(s)):
    if i<len(s)-1 and s[i] == s[i+1]:
        r += "$"
    else:
        r += s[i]
print(r)