'''
a
bc
d f
g  j
klmno
'''
n = int(input("n = "))
i=1
no = 1
while i<=n:
    j = 1
    while j<=i:
        if  i == n or j == i or j == 1:
            print(chr(96+no),end="")
            no+=1
        else:
            print(" ",end="")
            no+=1
        j+=1
    print()
    i+=1