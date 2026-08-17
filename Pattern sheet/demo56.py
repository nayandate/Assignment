'''
11111
 2222
  333
   44
    5
'''

n = int(input("n = "))
i = n
while i>=1:
    sp = 1
    while sp<=(n-i):
        print(" ",end="")
        sp+=1
    j = 1
    while j<=i:
         print(sp,end="")
         j+=1
    print()
    i-=1

