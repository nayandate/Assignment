'''
55555
 4444
  333
   22
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
         print(i,end="")
         j+=1
    print()
    i-=1

