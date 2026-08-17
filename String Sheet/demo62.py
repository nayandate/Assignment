'''
62. Count vowels and consonants. 
S = "apple" 
Vowels: 2, Consonants: 3
'''

s = input("String: ")
vow = 0
con = 0
for i in range(len(s)):
    if s[i].lower() in "aeiou":
        vow+=1
    if s[i].lower() in "sdfghjklzxcvbnmqwrtyp":
        con+=1 
print("Vowels:",vow)
print("Consonants:",con)