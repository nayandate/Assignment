'''
22. Find the last repeating character. 
S = "abracadabra" 
Output: 'r'
'''

s = "abracadabra"

check = ""

i = len(s) - 1
while i >= 0:
    if s[i] in check:
        print("Output:", s[i])
        break
    check+=s[i]
    i -= 1