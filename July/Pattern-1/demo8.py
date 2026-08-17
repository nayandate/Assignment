'''
8. n = 6

 654321
  65432
   6543
    654
     65

'''

n = int(input("Enter n = "))
i = 1
while i<=n-1:
      print()
      j = 1
      while j<=i:
          print(" ",end="")
          j+=1
      k = n
      while k>=i:
          print(k,end="")
          k = k-1
      i+=1

'''
for i in range(1,n):
      print()
      for j in range(1,i+1):
          print(" ",end="")
      for k in range(n,i-1,-1):
          print(k,end="")
'''


'''
Enter n = 5

 00000
  1111
   222
    33
     4
'''
'''
i = 1
while i<=n:
      print()
      j = 1
      while j<=i:
          print(" ",end="")
          j+=1
      k = n
      while k>=i:
          print(i-1,end="")
          k = k-1
      i+=1
'''