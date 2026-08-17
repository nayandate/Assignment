'''
*
**
* *
*  *
*****
'''

n = int(input("n = "))
i=1
no = 1
while i<=n:
    j = 1
    while j<=i:
        if i==n or j == i or j == 1:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1