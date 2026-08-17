'''
56. Reverse only consonants. 
S = "apple" 
"eplpa"
'''

s = input("String: ")
r=""
reverse = ""
for i in range(len(s)):
    if s[i] not in "aeiouAEIOU":
        reverse+=s[i]

j=len(reverse)-1
for k in range(len(s)):
    if s[k] not in "aeiouAEIOU":
        r+=reverse[j]
        j-=1
    else:
        r += s[k]
print("Ouput:",r)