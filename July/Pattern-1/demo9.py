'''
9. Pattern (n = 5)

    1
   10
  101
 1010
10101
'''

n = int(input("Enter number : "))

i = 1
while i<=n:
     print()
     j = n-1
     while j>=i:
         print(" ",end="")
         j = j-1
     k = 1
     while k<=i:
         if k%2 == 0:
             print("0",end="")
         else:
             print("1",end="")
         k = k+1
     i+=1