'''
74. Find the longest substring without repeating characters. 
S = "abcabcbb" 
"abc"
'''

s = input("Enter String: ")
vis = ""
ans = ""
for i in range(len(s)):
    count = 0
    for j in range(i+1,len(s)+1):
        y =s[i:j] 
        if y == y[::-1]:
            if len(y)>max:
                max = len(y)
                ans = y
print(ans)