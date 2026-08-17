'''
4.
=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================
'''


while True:
    print("\nPress 1 to Display Main Diagonal Elements")
    print("Press 2 to Display Secondary Diagonal Elements")
    print("Press 3 to Compare Main and Secondary Diagonal Sums")
    
    print("Press 4 for Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            rows = int(input("Enter number of rows for matrix: "))
            column = int(input("Enter number of columns for matrix: "))

            matrix=[]
            for i in range(rows):
                row=[]
                for j in range(column):
                    row.append(int(input("Enter elements for matrix: ")))
                matrix.append(row)
            print()
            print("Matrix :",matrix)
            print()
            print("Main Diagonal Elements:",end=" ")
            for i in range(rows):
                print(matrix[i][i],end=" ")

        case 2:
            rows = int(input("Enter number of rows for matrix: "))
            column = int(input("Enter number of columns for matrix: "))

            matrix=[]
            for i in range(rows):
                row=[]
                for j in range(column):
                    row.append(int(input("Enter elements for matrix: ")))
                matrix.append(row)
            print()
            print("Matrix :",matrix)
            print()
            print("Secondary Diagonal Elements:",end=" ")
            for i in range(rows):
                for j in range(column,0,-1):
                    print(matrix[i][j-1],end=" ")
                    column-=1
                    break            

        case 3:
            rows = int(input("Enter number of rows for matrix: "))
            column = int(input("Enter number of columns for matrix: "))

            matrix=[]
            for i in range(rows):
                row=[]
                for j in range(column):
                    row.append(int(input("Enter elements for matrix1: ")))
                matrix.append(row)
            print()
            print("Matrix :",matrix)
            print()
            sum1=0
            sum2=0
            for i in range(rows):
                sum1+=matrix[i][i]
            for i in range(rows):
                for j in range(column,0,-1):
                    sum2+=matrix[i][j-1]
                    column-=1
                    break    

            print("\nMain Diagonal Sum:",sum1)
            print("Secondary Diagonal Sum:",sum2)
            if sum1 == sum2:
                print("Both Diagonal Sums are Equal")
            else:
                print("Both Diagonal Sums are not Equal")
                
        case 4:
            print("Thank You for Using Matrix Diagonal Analysis System.")
            break
        case _:
            print("Wrong Choice")