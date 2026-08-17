'''
64. Count frequency of each vowel. 
S = "programming" 
o: 1, a: 1 (e, i, u: 0)
'''

s = input("Enter String: ")
x = "aeiou"
for j in range(len(x)):
    count = 0
    for k in range(len(s)):
        if x[j] == s[k]:
            count+=1
    print(x[j],":",count)