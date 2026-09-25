'''
Assignment 6: Electricity Bill Calculator

An electricity board wants to calculate a customer's electricity bill based on units consumed.

Create a class ElectricityBill with the following attributes:

Consumer number

Consumer name

Units consumed

Rate per unit

Fixed charge

Create the following methods:

calculate_energy_charge() – Calculate units × rate per unit.

calculate_total_bill() – Add energy charge and fixed charge.

display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600
'''

class ElectricityBill:
    def calculate_energy_charge(self,units,rate):
        self.units = units
        self.rate = rate
        self.energy = self.units * self.rate

    def calculate_total_bill(self,charge):
        self.charge = charge
        self.total = self.energy+charge

    def display_bill(self,num,name):
        print()
        print("Consumer Number:",num)
        print("Consumer Name:",name)
        print("Units Consumed:",self.units)
        print("Rate Per Unit:",self.rate)
        print("Fixed Charge:",self.charge)
        print("Energy Charge:",self.energy)
        print("Total Bill:",self.total)

cons_num = int(input("Enter Consumer Number: "))
cons_name = input("Enter Consumer Name: ")
units = int(input("Enter Unit Consumed: "))
rate = int(input("Enter Rate Per Unit: "))
charge = int(input("Enter Fixed Charge: "))

s1 = ElectricityBill()
s1.calculate_energy_charge(units,rate)
s1.calculate_total_bill(charge)
s1.display_bill(cons_num,cons_name)