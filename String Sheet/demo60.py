'''
60. Append two strings but remove adjacent duplicates. 
S1="miss", S2="issippi" 
"misisipi"
'''

s1 = input("String1: ")
s2 = input("String2: ")
s = s1+s2
r = ""
for i in range(len(s)):
    if (s[i-1] != s[i]) or i == 0:
        r+=s[i]
print(r)