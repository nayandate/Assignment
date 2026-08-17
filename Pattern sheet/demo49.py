'''
    1
   10
  101
 1010
10101
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
        if i%2==0:
            if k%2==0:
                print("0",end="")
            else:
                print("1",end="")
        else:
            if k%2==0:
                print("0",end="")
            else:
                print("1",end="")
        k+=1
    print()
    i+=1


