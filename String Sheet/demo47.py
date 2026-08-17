'''
47. Check for substring using concatenation trick. 
S1="CDAB", S2="ABCD" 
True (S1 is in S2+S2)
'''

sub = input("Substring: ")
s = input("String: ")

if sub in s+s:
    print("True")
else:
    print("False")