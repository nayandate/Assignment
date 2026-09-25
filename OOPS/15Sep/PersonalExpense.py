'''
Assignment 10: Personal Expense Calculator

A person wants to calculate monthly expenses and savings.

Create a class ExpenseTracker with the following attributes:

Person name

Monthly salary

Rent

Food expenses

Travel expenses

Other expenses

Create the following methods:

calculate_total_expenses() – Calculate all expenses.

calculate_savings() – Calculate salary minus total expenses.

display_expense_report() – Display salary, expenses, and savings.

Formula:

Total Expenses = Rent + Food + Travel + Other Expenses
Savings = Monthly Salary - Total Expenses

Sample data:

Monthly Salary: 60000
Rent: 12000
Food: 8000
Travel: 5000
Other Expenses: 3000

Expected result:

Total Expenses: 28000
Savings: 32000
'''

class ExpenseTracker:
    def calculate_total_expenses(self,rent,food,travel,other):
        self.rent = rent
        self.food = food
        self.travel = travel
        self.other = other
        self.total = rent+food+travel+other

    def calculate_savings(self,sal):
        self.sal = sal
        self.save = sal - self.total

    def display_expense_report(self):
        print()
        print("Total Expenses: ",self.total)
        print("Savings: ",self.save)

s1 = ExpenseTracker()

name = input("Enter Person Name: ")
sal = int(input("Enter Salary: "))
rent = int(input("Enter Rent: "))
food = int(input("Enter Food Expenses: "))
travel = int(input("Enter Travel Expenses: "))
other = int(input("Enter Other Expenses: "))

s1.calculate_total_expenses(rent,food,travel,other)
s1.calculate_savings(sal)
s1.display_expense_report()