'''
a
ab
abc
abcd
abcde
'''

n = int(input("n = "))
i=1
while i<=n:
    j = 1
    while j<=i:
        print(chr(96+j),end = "")
        j+=1
    print()
    i+=1