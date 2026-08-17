'''
    5
   44
  333
 2222
11111
'''

n = int(input("n = "))
l=n
i=1
while i<=n: 
    j = 1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k=i
    while k>=1:
        print(l,end="")
        k-=1
    l-=1
    print()
    i+=1