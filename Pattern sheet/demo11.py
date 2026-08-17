'''
A
AB
ABC
ABCD
ABCDE
'''

n = int(input("n = "))
i=1
while i<=n:
    j = 1
    while j<=i:
        print(chr(64+j),end = "")
        j+=1
    print()
    i+=1