# 1. WAP to print matrix element row wise.
'''
matrix = [
[1,2,3],
[32,4,8],
[9,66,77]
]

for row in matrix:
    print(*row)
'''

# 2. WAP to print element of matrix.
'''
matrix = [
[1,2,3],
[32,4,8],
[9,66,77]
]

for row in matrix:
    for value in row:
          print(value,end=" ")
    print()
'''

# 3. WAP to print only even element of a matrix.
'''
matrix = [
[1,2,3],
[2,4,8],
[9,6,7]
]

for row in matrix:
    for value in row:
          if value%2==0:
              print(value,end=" ")
          else:
              print(" ",end=" ")
    print()
'''

# 4. WAP to read rows and columns from user and elements and display.
'''
rows = int(input("Enter size of rows: "))
columns = int(input("Enter size of columns: "))
matrix = []
print("Enter elements of matrix: ")
for i in range(rows):
      row=[]
      for j in range(columns):
            row.append(int(input()))
      matrix.append(row)

print("Matrix Elements:")
for row in matrix:
    for value in row:
          print(value,end=" ")
    print()
'''

# 5. WAP to read matrix from user and then display sum of all elements in a matrix.
'''
rows = int(input("Enter size of rows: "))
columns = int(input("Enter size of columns: "))
matrix = []
sum=0
print("Enter elements of matrix: ")
for i in range(rows):
      row=[]
      for j in range(columns):
            row.append(int(input()))
      matrix.append(row)

print("Matrix Elements:")
for row in matrix:
    for value in row:
          print(value,end=" ")
    print()

for row in matrix:
    for value in row:
          sum+=value
print("Sum:",sum)
'''