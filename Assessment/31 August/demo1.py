'''
QNO 1: Matrix Transpose & Diagonal Transformation(3.5 marks)

Write a Python program that accepts an N × N square matrix from the user.

The program must:

Display the original matrix.
Find and display the Main Diagonal elements.
Find and display the Secondary Diagonal elements.
Create the transpose of the matrix.
In the transposed matrix, swap each Main Diagonal element with the corresponding Secondary Diagonal element.
Display the final matrix.
The original matrix must not be modified.
Input
Enter the size of matrix: 4

Enter matrix elements:
10 20 30 40
50 60 70 80
90 15 25 35
45 55 65 75
Expected Output
Original Matrix:
10 20 30 40
50 60 70 80
90 15 25 35
45 55 65 75

Main Diagonal Elements:
10 60 25 75

Secondary Diagonal Elements:
40 70 15 45

Transpose Matrix:
10 50 90 45
20 60 15 55
30 70 25 65
40 80 35 75

Final Matrix After Diagonal Swapping:
45 50 90 10
20 15 60 55
30 25 70 65
75 80 35 40


Conditions
Use Python nested lists.
Matrix size must be taken from the user.
Do not use NumPy.
Do not use zip().
Do not use built-in matrix operations.
Do not modify the original matrix.

'''
row = int(input("Enter no. of rows: "))
col = int(input("Enter no. of columns: "))
mat = []
for i in range(row):
    ans = []
    for j in range(col):
        element = int(input("Enter element: "))
        ans.append(element)
    mat.append(ans)
print(mat)

print()
print("Main Diagonal Elements:")
main = []
for i in range(row):
    for j in range(col):
        if i == j:
            print (mat[i][j],end=" ")
            main.append(mat[i][j])

print()
print("\nSecondary Diagonal Elements:")
secondary = []
for i in range(row):
    secondary.append(mat[i][row-1-i])
    print(mat[i][row-1-i],end=" ")

print()
transpose = []
for i in range(row):
    rows = []
    for j in range(col):
         rows.append(mat[j][i])
    transpose.append(rows)
print()
print("transpose: ")
for i in range(row):
    for j in range(col):
      print(transpose[i][j],end=" ")
    print()

print()
for i in range(row):
    temp = transpose[i][i]
    transpose[i][i] = transpose[i][row-1-i]
    transpose[i][row-1-i] = temp
print("Final Matrix After Diagonal Swapping:")
for i in range(row):
    for j in range(col):
        print(transpose[i][j], end=" ")
    print()








