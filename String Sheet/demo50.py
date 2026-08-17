'''
50. Remove all digits. 
S = "a1b2c3" 
"abc"
'''

s = input("String: ")
r=""
for i in range(len(s)):
    if "0" <= s[i] <= "9":
        r += ''
    else:
        r += s[i]
print(r)