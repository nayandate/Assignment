'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''

n = int(input("n = "))
i = 1
while i<=n:
    sp = n
    while sp>i:
        print(" ",end="")
        sp-=1
    j = 1
    while j<=i:
         print(j,"",end="")
         j+=1
    print()
    i+=1

