'''
5
54
543
5432
54321
'''

n = int(input("n = "))
i=1
while i<=n:
    j = 1
    while j<=i:
        print(n+1-j,end="")
        j+=1
    print()
    i+=1