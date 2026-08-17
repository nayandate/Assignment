'''
57. Merge two strings alternatively. 
S1 = "ABC", S2 = "def" 
"AdBeCf"
'''

s1 = input("String1: ")
s2 = input("String2: ")
if len(s1)>len(s2):
    x = s1
    y = s2
else:
    x = s2
    y = s1
r = ""
for i in range(len(x)):
    if i<len(y):
        r+=s1[i]+s2[i]
    else:
        r+=x[i]
print("Ouput:",r)