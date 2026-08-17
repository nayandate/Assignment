'''
55555
 4__4
  3_3
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
         if j == i or j == 1 or i == n:
             print(i,end="")
         else:
            print("_",end="")
         j+=1
    print()
    i-=1

