'''
3.
=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

=========================================================
'''

while True:
    print("\nPress 1 to Count Armstrong Numbers Row-wise")
    print("Press 2 to Count Palindrome Numbers Column-wise")
    print("Press 3 to Display Average of Each Row")
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
            for i in range(rows):
                count = 0
                for j in range(column):
                    sum=0
                    x=0
                    n=matrix[i][j]
                    temp = n
                    while n > 0:
                        x+=1
                        n=n//10
                    n = temp
                    while n>0:
                        rem = n%10
                        sum+=rem**(x)
                        n = n//10

                    if sum == temp:
                        count+=1
                print("Row",i+1,"Armstrong Count:",count)

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
            for i in range(rows):
                count = 0
                for j in range(column):
                    sum=0
                    n=matrix[j][i]
                    temp=n
                    rev = 0
                    while n>0:
                        rev = rev*10+n%10
                        n=n//10
                    if rev == temp:
                        count+=1
                print("Column",i+1,"Palindrome Count:",count)
            

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
            for i in range(rows):
                sum = 0
                for j in range(column):
                    sum+=matrix[i][j]
                print("Row",i+1,"Average:",(sum//column)) 
        case 4:
            print("Thank You for Using Matrix Quality Check System.")
            break
        case _:
            print("Wrong Choice")