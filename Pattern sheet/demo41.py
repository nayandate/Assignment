'''
A
BCD
EFGHI
JKLMNOP
'''

n = int(input("n = "))
l = 1
i=1
k=1
while i<=n: 
    j = 1
    while j<=l:
        print(chr(64+k),end="")
        j+=1
        k+=1
    l+=2
    print()
    i+=1