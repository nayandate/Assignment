'''
72. Print all substrings of length n. 
S = "abc", n = 2 
"ab, bc"
'''

s = input("String: ")
n = int(input("Enter n: "))
for ch in range(len(s)):
    for i in range(ch+1,len(s)+1):
        if len(s[ch:i]) == n:
            print(s[ch:i],end=", ")