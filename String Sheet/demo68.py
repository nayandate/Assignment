'''
68. Count the sum of digits present in a string. 
S = "a1b2c3" 
6 (1+2+3)
'''

s = input("String: ")
sum=0
for ch in s:
    if '0'<=ch<='9':
        sum+=int(ch)
print("Sum:",sum)