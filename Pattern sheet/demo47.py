'''
    1
   11
  1*1
 1**1
11111
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
        if i == n or k == 1 or k == i:
            print("1",end="")
        else:
            print("*",end="")
        k+=1
    print()
    i+=1