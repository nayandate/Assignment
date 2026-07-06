'''
4. Pattern

1
00
111
0000
11111
'''

n = int(input("Enter n = "))
i = 1
while i<=n:
      print()
      j = 1
      while i>=j:
          if i%2==0:
              print("0",end="")
          else:
              print("1",end="")
          j = j+1
      i+=1