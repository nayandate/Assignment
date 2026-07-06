'''
5. Pattern

A
AB
ABC
ABCD
ABCDE
'''

n = int(input("Enter n = "))
i = 1
while i<=n:
      print()
      j = 1
      while i>=j:
          print(chr(64+j),end="")
          j = j+1
      i+=1