'''
73. Find the longest palindromic substring. 
S = "babad" 
"bab" (or "aba")
'''

s = input("Enter String: ")
max=0
ans=""
for i in range(len(s)):
    count = 0
    for j in range(i+1,len(s)+1):
        y =s[i:j] 
        if y == y[::-1]:
            if len(y)>=max:
                max = len(y)
                ans = y
print(ans)