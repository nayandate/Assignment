'''
6. Pattern
a
ab
abc
abcd
abcde
'''

n = int(input("Enter n = "))
i = 1
while i<=n:
      print()
      j = 1
      while i>=j:
          print(chr(96+j),end="")
          j = j+1
      i+=1