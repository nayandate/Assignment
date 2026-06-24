'''
1. Electricity Department Billing System


The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250

Output:
Total Electricity Bill: ₹1950
'''

unit = int(input("Enter units consumed: "))
if unit<=100 :
         print("Total Electricity Bill: ₹",unit*5)
elif unit<=200 :
         bill = (unit-100)*7+100*5
         print("Total Electricity Bill: ₹",bill)
else :
         bill = (unit-200)*10+100*7+100*5
         print("Total Electricity Bill: ₹",bill)
