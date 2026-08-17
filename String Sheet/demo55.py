'''
55. Reverse only vowels. 
S = "hello" 
"holle"
'''
s = input("String: ")
r=""
reverse = ""
for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        reverse+=s[i]

j=len(reverse)-1
for k in range(len(s)):
    if s[k] in "aeiouAEIOU":
        r+=reverse[j]
        j-=1
    else:
        r += s[k]
print("Ouput:",r)