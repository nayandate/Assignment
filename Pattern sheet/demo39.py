'''
123456
54321
1234
321
12
1
'''

n = int(input("n = "))
l = n+1
i=n
while i>=1: 
    j = 1
    while j<=i:
        if i%2==0:
            print(j,end="")
        else:
            print(l-j,end="")
        j+=1
    l=l-1
    print()
    i-=1