'''
    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI

'''

n = int(input("n = "))
i = 1
while i<=n:
    sp = n
    while sp>i:
        print(" ",end="")
        sp-=1
    j = 1
    while j<=i*2-1:
          print(chr(64+j),end="")
          j+=1
    print()
    i+=1

