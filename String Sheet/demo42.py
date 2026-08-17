'''
42. Check if two strings are equal without equals(). 
S1 = "abc", S2 = "abc" 
TRUE
'''

s1 = input("String1 : ")
s2 = input("String2 : ")

if len(s1) != len(s2):
    print("FALSE")
else:
    match=1
    i = 0
    while i<len(s2):
         if s1[i]!=s2[i]:
              match=0
              break
         i+=1
    if match !=1:
         print("FALSE")
    else:
         print("TRUE")