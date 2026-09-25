'''
54. Replace all duplicate chars with '$'. 
S = "hello" 
"he$lo"
'''

s = input("String: ")
r=""
x=0
for i in range(len(s)):
    if i<len(s)-1 and s[i] == s[i+1]:
        if x == 0:
            r += "$"
            x=1
        else:
            r+=s[i]
    else:
        r += s[i]
print(r)