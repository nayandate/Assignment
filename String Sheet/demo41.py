'''
41. Check if a string contains a substring (without using built-in method). 
S1 = "Hello", Sub="ell" 
TRUE
'''
'''
s = input("String: ")
word = input("Word: ")
if word in s:
     print("True")
else:
     print("False")
'''

s = input("String: ")
word = input("Word: ")
match=0

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