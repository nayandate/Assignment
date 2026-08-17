'''
53. Remove punctuation. 
S = "Hello, world!" 
"Hello world"
'''

s = input("String: ")
r=""
for i in range(len(s)):
    if s[i] in ".,?!;:-_()[]{}'":
        r += ''
    else:
        r += s[i]
print(r)