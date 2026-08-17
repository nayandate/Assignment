'''
EEEEE
DDDD
CCC
BB
A
'''

n = int(input("n = "))
i=n
while i>=1:
    j = 1
    while j<=i:
        print(chr(64+i),end="")
        j+=1
    print()
    i-=1