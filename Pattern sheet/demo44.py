'''
    1
   22
  333
 4444
55555
'''

n = int(input("n = "))
i=1
while i<=n: 
    j = 1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k = 1
    while k<=i:
        print(i,end="")
        k+=1
    print()
    i+=1