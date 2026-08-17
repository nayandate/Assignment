'''
48. Remove all vowels. 
S = "aeiou XYZ" 
" XYZ"
'''
s = input("String: ")
r=""
for i in range(len(s)):
    if s[i] not in "aeiouAEIOU":
        r += s[i]
print(r)