'''
49. Replace all consonants with '*' (Example suggests replacing non-vowels). 
S = "apple" 
"ap*le" (or similar output depending on implementation)
'''

s = input("String: ")
r=""
for i in range(len(s)):
    if s[i] not in "aeiouAEIOU":
        r += '*'
    else:
        r += s[i]
print(r)