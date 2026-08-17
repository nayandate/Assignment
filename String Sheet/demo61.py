'''
61. Count total alphabets, digits, and special characters. 
S = "a1b!c2" 
Alphabets: 3, Digits: 2, Special: 1
'''

s = input("String: ")
alp = 0
dig = 0
spe = 0

for i in range(len(s)):
    if "0"<=s[i]<="9":
        dig+=1
    elif "a"<=s[i].lower()<="z":
        alp+=1
    elif s[i] in "@!#$%&":
        spe+=1 
print("Alphabets:",alp)
print("Digits:",dig)
print("Special:",spe)