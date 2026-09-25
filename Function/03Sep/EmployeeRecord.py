'''
1. Employee Record Sorting (Lambda)
A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.
Task:
Write a Python program to sort the employee records using a lambda expression.
Input:
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
Output:
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]
'''

employee=[]
n = int(input("Enter no. of employee: "))
for i in range(n):
    name = input(f"Enter name of employee {i+1}: ")
    sal = int(input(f"Enter salary of employee {i+1}: "))
    a=(name,sal)
    employee.append(a)
print("Employees: ",employee)
result=sorted(employee,key=lambda x:x[1])
print(result)