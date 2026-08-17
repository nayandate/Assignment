'''
ABCDE
ABCD
ABC
AB
A
'''

n = int(input("n = "))
i=n
while i>=1:
    j = 1
    while j<=i:
        print(chr(64+j),end="")
        j+=1
    print()
    i-=1