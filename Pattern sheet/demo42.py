'''
54321
5432
543
54
5
'''

n = int(input("n = "))
i=1
while i<=n: 
    j = n
    while j>=i:
        print(j,end="")
        j-=1
    print()
    i+=1