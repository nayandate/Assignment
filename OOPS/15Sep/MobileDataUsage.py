'''
Assignment 7: Mobile Phone Data Usage

A mobile user wants to calculate their remaining internet data.

Create a class MobilePlan with the following attributes:

Customer name

Mobile number

Total data in GB

Used data in GB

Validity in days

Create the following methods:

calculate_remaining_data() – Calculate remaining data.

calculate_usage_percentage() – Calculate the percentage of data used.

display_plan() – Display the plan details and results.

Sample data:

Total Data: 50 GB
Used Data: 18 GB
Validity: 28 days

Expected result:

Remaining Data: 32 GB
Usage Percentage: 36.0%
'''

class MobilePlan:
    def calculate_remaining_data(self,total,used):
        self.total = total
        self.used = used
        self.rem = total - used

    def calculate_usage_percentage(self):
        self.usage_per = (self.used/self.total)*100

    def display_plan(self,name,num,val):
        print()
        print("Customer name:",name)
        print("Mobile number:",num)
        print("Total Data:",self.total)
        print("Used Data:",self.used)
        print("Validity:",val)
        print("Remaining Data:",self.rem)
        print(f"Usage Percentage: {self.usage_per}%")

name = (input("Customer name: "))
num  = int(input("Mobile number: "))
total_data = int(input("Total data in GB: "))
used_data = int(input("Used data in GB: "))
val = int(input("Validity in days: "))

s1 = MobilePlan()
s1.calculate_remaining_data(total_data,used_data)
s1.calculate_usage_percentage()
s1.display_plan(name,num,val)