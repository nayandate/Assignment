'''
63. Count frequency of each character. 
S = "aabcc" 
a: 2, b: 1, c: 2
'''

s = input("Enter String: ")
x=""
for i in range(len(s)):
    if s[i] not in x:
        x+=s[i]

for j in range(len(x)):
    count = 0
    for k in range(len(s)):
        if x[j] == s[k]:
            count+=1
    print(x[j],":",count)