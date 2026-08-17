'''
ABCDE
 A__D
  A_C
   AB
    A
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
         if j == i or j == 1 or i == n:
             print(chr(64+j),end="")
         else:
            print("_",end="")
         j+=1
    print()
    i-=1

