'''
10. Trim leading, trailing, or extra spaces.
'''

s = input("Input: ")
result=""
s = s.strip()

i = 0
while i<len(s):
    if s[i-1] == " ":
        if ((s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z')) and s[i-1] == " ":
            result += ""+s[i]
    else:
            result +=s[i]
    i+=1
print(result)