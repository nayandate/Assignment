'''
A
BB
CCC
DDDD
EEEEE
'''

n = int(input("n = "))
i=1
while i<=n:
    j = 1
    while j<=i:
        print(chr(64+i),end="")
        j+=1
    print()
    i+=1