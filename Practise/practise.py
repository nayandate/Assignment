'''
5. Minimum Window Substring
Given strings s and t, find the smallest substring of s that contains all characters of t (with counts).
s = "ADOBECODEBANC", t = "ABC" → "BANC"
'''

s = input("Enter String: ")
t = input("Enter Sub-String: ")
min = len(s)+1
result = ""
for i in range(len(s)):
    for j in range(i+1,len(s)):
        st = s[i:j+1]

        x=1
        for k in t:
            if t.count(k)>st.count(k):
                x=0
                break
        if x==1:
            if len(st)<min:
                min = len(st)
                result = st
print(result)