'''
38. Reverse words without split(). 
S = "a b c" 
"c b a"
'''
'''
s=input("Input: ")
result=""
i=len(s)-1
while i>=0:
    result+=s[i]
    i-=1
print(result)

'''
s = input("String: ")
r = ""
word = ""

i = len(s)-1

while i >= 0:
    if s[i] == " ":
        j = len(word) - 1
        while j >= 0:
            r += word[j]
            j -= 1
        r += " "
        word = ""
    else:
        word += s[i]
    i -= 1

j = len(word) - 1
while j >= 0:
    r += word[j]
    j -= 1
print(r)
