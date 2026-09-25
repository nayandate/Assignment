'''
Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0
'''

class Employee:
    def __init__(self,employee_id,employee_name,basic_salary):
        self.id = employee_id
        self.name = employee_name
        self.sal = basic_salary

    def hra(self):
        self.hrallow = self.sal * 20/100

    def da(self):
        self.daily = self.sal * 0.15

    def gross(self):
        self.gross = self.sal + self.hrallow + self.daily

    def display(self):
        print(f'''
------ Employee Salary Details ------
Employee ID      : {self.id}
Employee Name    : {self.name}
Basic Salary     : {self.sal}
HRA              : {self.hrallow}
DA               : {self.daily}
Gross Salary     : {self.gross}''')


employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ") 
basic_salary = float(input("Enter Basic Salary: "))

s1 = Employee(employee_id,employee_name,basic_salary)

s1.hra()
s1.da()
s1.gross()
s1.display()