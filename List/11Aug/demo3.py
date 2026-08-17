'''
3. MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 - Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 - Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 - Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''

while True:
    print("""
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit""")

    choice = int(input("Enter your Choice:"))
    match choice:

        case 1:
            r = int(input("Enter size of matrix :"))

            A = []
            for i in range(r):
                row = []
                print("Enter score of",i+1,"Employee:")
                for j in range(r):
                    row.append(int(input("scores:")))
                A.append(row)
            max = 0
            index = 0
            for i in range(len(A)):
                s = sum(A[i])
                if s > max:
                    max = s
                    index = i
            print("Employee",index+1,"has Highest Total Score =",max)
            
            
        case 2:

            r = int(input("Enter size of matrix :"))

            A = []
            for i in range(r):
                row = []
                print("Enter score of",i+1,"Employee:")
                for j in range(r):
                    row.append(int(input("scores:")))
                A.append(row)
                     
            
            for col in range(len(A[0])):
                avg = 0
                for row in A:
                    avg += row[col]
                ans = avg//r
                
                print("Employee",col+1,"Average =",ans)


        case 3:

            r = int(input("Enter size of matrix :"))

            A = []
            for i in range(r):
                row = []
                print("Enter score of",i+1,"Employee:")
                for j in range(r):
                    row.append(int(input("scores:")))
                A.append(row)

            index = 1
            for i in A:
                print("Employee",index,"Max Score =",max(i))
                index+=1

        case 4:
            print("Thank You for Using MATRIX PERFORMANCE EVALUATION SYSTEM")
            break

        case __:
            print("Invalid Case")