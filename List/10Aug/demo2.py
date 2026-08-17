'''
2. =========================================================
                MATRIX ANALYSIS SYSTEM
   =========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System
=========================================================
'''

while True:
    print("\nPress 1 to Count Prime Numbers Row-wise")
    print("Press 2 to Count Perfect Numbers Column-wise")
    print("Press 3 to Display Row-wise Sum")
    print("Press 4 for Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            print("---------------------------------------------------------")
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
            for i in range(rows):
                count = 0
                for j in range(column):
                    x=0
                    n=matrix[i][j]
                    if n<1:
                        x=1 
                    for k in range(2,(n//2)+1):
                        if n%k==0:
                            x=1
                            break
                    if x!=1:
                        count+=1
                print("Row",i+1,"Prime Count:",count)

        case 2:
            print("---------------------------------------------------------")
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
            for i in range(rows):
                count = 0
                for j in range(column):
                    sum=0
                    n=matrix[j][i]
                    for k in range(1,(n//2)+1):
                        if n%k==0:
                            sum+=k
                    if sum == n:
                        count+=1
                print("Column",i+1,"Perfect Number Count:",count)

        case 3:
            print("---------------------------------------------------------")
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
            for i in range(rows):
                sum = 0
                for j in range(column):
                    sum+=matrix[i][j]
                print("Row",i+1,"Sum:",sum) 
        case 4:
            print("Thank You for Using Matrix Analysis System.")
            print("=========================================================")
            break
        case _:
            print("Wrong Choice")