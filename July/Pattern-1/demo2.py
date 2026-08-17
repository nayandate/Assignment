'''
2. WAP to print Square, Cube and Square Root of all numbers from 1 to N
'''
import math
n = int(input("Enter a number to print Square, Cube and Square Root of all numbers from 1 to : "))
i = 1
while i<=n:
      sq = i*i
      cb = i*i*i
      sqrt = float(math.sqrt(i))
      print(i," -> ","Square = ",sq,"\n       Cube = ",cb,"\n       Square Root = ",round(sqrt,2))
      i+=1
