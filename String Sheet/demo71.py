'''
71. Print all substrings. 
S = "abc" 
"a, b, c, ab, bc, abc"
'''

s = input("String: ")

for ch in range(1,len(s)+1):
    for i in range(len(s)-ch+1):
        print(s[i:i+ch], end=", ")