'''
58. Rotate characters left by 2 positions. 
S = "abcde" 
"cdeab"
'''

s = input("String: ")
n = int(input("Positions to left rotate: "))
n = n % len(s)
r = s[n:] + s[:n]
print("Output:", r)