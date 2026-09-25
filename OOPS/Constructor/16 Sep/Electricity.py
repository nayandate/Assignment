'''
Question 2: Electricity Bill Calculator
Scenario

An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0'''


class Customer:
    def __init__(self,id,name,unit):
        self.id = id
        self.name = name
        self.unit = unit

    def bill(self):
        self.bill = (self.unit * 8) +150.0

    def display(self):
        print(f"""
------ Electricity Bill ------
Customer ID       : {self.id}
Customer Name     : {self.name}
Units Consumed    : {self.unit}
Total Bill Amount : ₹{self.bill}""")


customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
units_consumed = int(input("Enter Units Consumed: "))

s1 = Customer(customer_id,customer_name,units_consumed)
s1.bill()
s1.display()