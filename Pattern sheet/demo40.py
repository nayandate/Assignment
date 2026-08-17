'''
*
**
****
*******
***********
'''

n = int(input("n = "))
l = 1
i=1
while i<=n: 
    j = i
    while j<=l:
        print("*",end="")
        j+=1
    l=l+i+1
    print()
    i+=1