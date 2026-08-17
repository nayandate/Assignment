'''
    A
   A B
  A B C
 A B C D
A B C D E  
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
         print(chr(64+j),"",end="")
         j+=1
    print()
    i+=1

