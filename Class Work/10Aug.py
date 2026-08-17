# 1. WAP to find maximum element in matrix.
'''
m=[[1,2,3],[5,6,7]]
max=m[0][0]
for row in m:
   for v in row:
       if max<v:
           max=v
print(max)
'''

# 2. WAP to print main diagonal sum.
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

print("Matrix Elements:",matrix)

sum=0
for j in range (len(matrix)):
       sum+=matrix[j][j]
print("Sum is:",sum)
'''

# 3. WAP to count even no. in a matrix.
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

print("Matrix Elements:",matrix)

count=0
for i in range (len(matrix)):
     for j in range(len(matrix[i])):
       if matrix[i][j]%2==0:
             count+=1
print("Count is:",count)
'''

# 4. WAP to to search an element in a matrix and display its index.
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
print("Matrix Elements:",matrix)

search = int(input("Enter element to search: "))
for i in range (len(matrix)):
     for j in range(len(matrix[i])):
       if matrix[i][j]==search:
             print("Found:")
             print("Index:","row",i,"column",j)
             break
'''

# 5. WAP to add two matrices.
'''
rows1 = int(input("Enter size of rows for matrix1: "))
columns1 = int(input("Enter size of columns for matrix1: "))

rows2 = int(input("Enter size of rows for matrix2: "))
columns2 = int(input("Enter size of columns for matrix2: "))

if rows1==rows2 and columns1==columns2:
      matrix1 = []
      sum=0
      print("Enter elements of matrix1: ")
      for i in range(rows1):
            row1=[]
            for j in range(columns1):
                  row1.append(int(input()))
            matrix1.append(row1)
      
      matrix2 = []
      sum=0
      print("\nEnter elements of matrix2: ")
      for i in range(rows2):
            row2=[]
            for j in range(columns2):
                  row2.append(int(input()))
            matrix2.append(row2)
      print("\nMatrix 1:",matrix1)
      print("\nMatrix 2:",matrix2)
      
      matrix=matrix1
      for i in range (len(matrix1)):
           for j in range(len(matrix1[i])):
              matrix[i][j]=matrix1[i][j]+matrix2[i][j]
      print("\nAddition is ",matrix)

else:
      print("\nOperation is not possible for 2 different matrixes whose rows and columns are different from each other.")
'''

# 6. WAP to add two matrices.
'''
rows1 = int(input("Enter size of rows for matrix1: "))
columns1 = int(input("Enter size of columns for matrix1: "))

rows2 = int(input("Enter size of rows for matrix2: "))
columns2 = int(input("Enter size of columns for matrix2: "))

if rows1==rows2 and columns1==columns2:
      matrix1 = []
      sum=0
      print("Enter elements of matrix1: ")
      for i in range(rows1):
            row=[]
            for j in range(columns1):
                  row.append(int(input()))
            matrix1.append(row)
      
      matrix2 = []
      sum=0
      print("\nEnter elements of matrix2: ")
      for i in range(rows2):
            row=[]
            for j in range(columns2):
                  row.append(int(input()))
            matrix2.append(row2)
      print("\nMatrix 1:",matrix1)
      print("\nMatrix 2:",matrix2)
      
      matrix=matrix1
      for i in range (len(matrix1)):
           for j in range(len(matrix1[i])):
              matrix[i][j]=matrix1[i][j]+matrix2[i][j]
      print("\nAddition is ",matrix)

else:
      print("\nOperation is not possible for 2 different matrixes whose rows and columns are different from each other.")
'''

'''
# 6. WAP to multiply two matrices.
Condition:
    Suppose we have 2 matrices 
        Matrix A:
           rows = r1
           columns = c1

        Matrix B:
           rows = r2
           columns = c2
    Matrix multiplication is possible only :
        c1 = r2
Note: Size of result matrix will be r1*c2
       
'''

rows1 = int(input("Enter size of rows for matrix1: "))
columns1 = int(input("Enter size of columns for matrix1: "))

rows2 = int(input("Enter size of rows for matrix2: "))
columns2 = int(input("Enter size of columns for matrix2: "))

if columns1==rows2:
      matrix1 = []
      print("Enter elements of matrix1: ")
      for i in range(rows1):
            row=[]
            for j in range(columns1):
                  row.append(int(input()))
            matrix1.append(row)
      
      matrix2 = []
      print("\nEnter elements of matrix2: ")
      for i in range(rows2):
            row=[]
            for j in range(columns2):
                  row.append(int(input()))
            matrix2.append(row)
      print("\nMatrix 1:",matrix1)
      print("\nMatrix 2:",matrix2)
      
      matrix = []
      for i in range(rows1):
            row=[]
            for j in range(columns2):
                  row.append(0)
            matrix.append(row)

      for i in range (rows1):
            for j in range(columns2):
                  for k in range(columns1):
                        matrix[i][j]=matrix[i][j]+matrix1[i][k]*matrix2[k][j]
      print("\nResult is ",matrix)

else:
      print("\nOperation is not possible for 2 different matrixes whose rows and columns are different from each other.")
