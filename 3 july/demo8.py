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