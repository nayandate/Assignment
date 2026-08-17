'''
65. Count palindromic substrings. 
S = "aaa" 
6 (a, a, a, aa, aa, aaa)
'''

s = input("String: ")
count = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1]:
            count += 1
print(count)