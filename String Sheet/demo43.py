'''
43. Check if two strings are rotations of each other. 
S1 = "abcde", S2 = "cdeab" 
TRUE
'''

s = input("String: ")
word = input("Word: ")
match=0
s=s+s

i = 0
while i<=len(s)-len(word):
    j = 0
    while j < len(word):
        if s[i + j] != word[j]:
            break
        j += 1

    if len(word)==j:
        match=1
        break
    i += 1

if match==1:
    print("TRUE")
else:
    print("FALSE")