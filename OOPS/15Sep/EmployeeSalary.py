'''
Assignment 2: Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:

Employee ID

Employee name

Basic salary

HRA percentage

DA percentage

Create the following methods:

calculate_hra() - Calculate HRA.

calculate_da() - Calculate DA.

calculate_gross_salary() - Calculate gross salary.

display_salary() - Display employee salary details.

Formula:

HRA = Basic Salary * HRA Percentage / 100
DA = Basic Salary * DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA
'''

class Employee:
    def calculate_hra(self,sal,hra_per):
        self.sal = sal
        self.hra_per = hra_per
        self.hra = (sal * hra_per)/100

    def calculate_da(self,sal,da_per):
        self.da_per = da_per
        self.da = (sal * da_per)/100

    def calculate_gross_salary(self):
        self.gross = self.sal + self.hra + self.da

    def display_salary(self,id,name):
        print()
        print("Employee ID:",id)
        print("Employee Name:",name)
        print("HRA :",self.hra)
        print("DA :",self.da)
        print("Gross Salary:",self.gross)

s1 = Employee()

id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
sal = int(input("Enter Basic Salary: "))
hra = float(input("Enter HRA Percentage: "))
da = float(input("Enter DA Percentage: "))

s1.calculate_hra(sal,hra)
s1.calculate_da(sal,da)
s1.calculate_gross_salary()
s1.display_salary(id,name)