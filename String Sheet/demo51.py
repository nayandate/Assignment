'''
51. Extract only digits. 
S = "a1b2c3" 
"123"
'''

s = input("String: ")
r=""
for i in range(len(s)):
    if "0" <= s[i] <= "9":
        r += s[i]
    else:
        r += ''
print(r)