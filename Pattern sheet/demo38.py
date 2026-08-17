'''
55555
4  4
3 3
22
1
'''

n = int(input("n = "))
i=n
while i>=1:
    j = 1
    while j<=i:
        if n==i or j == 1 or j == i:
            print(i,end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i-=1