'''
59. Rotate characters right by 3 positions. 
S = "abcde" 
"cdeab"
'''

s = input("String: ")
n = int(input("Positions to right rotate: "))
n = n % len(s)
r = s[-n:] + s[:-n]
print("Output:", r)