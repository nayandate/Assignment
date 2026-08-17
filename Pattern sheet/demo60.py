'''
    X 
   X X 
  X___X
 X_____X
X X X X X
 
'''

n = int(input("n = "))
i = 1
while i<=n:
    sp = n
    while sp>i:
        print(" ",end="")
        sp-=1
    j = 1
    while j<=2*i-1:
      if j == 1 or j == i or i == n or i == 1:
          print("X",end=" ")
      else:
         print("__",end="")
      j+=1
    print()
    i+=1

