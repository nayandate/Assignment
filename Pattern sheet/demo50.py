'''
12345
 1234
  123
   12
    1
'''

n = int(input("n = "))
i = n
k = 1
while i>=1:
    sp = 1
    while sp<k:
        print(" ",end="")
        sp+=1
    k+=1
    j = 1
    while j<=i:
         print(j,end="")
         j+=1
    print()
    i-=1

