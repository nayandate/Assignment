# 1. 
'''
a = [
    [
      [1,2],
      [3,4]
    ],
    [
      [6,7],
      [8,9]
    ]
    ]
print(a)
'''

# 2. WAP to read employee details from user and store them as tuple.
'''
id = int(input("Enter id: "))
name = input("Enter name: ")
dept = input("Enter department: ")
sal = int(input("Enter salary: "))

employee=(id,name,dept,sal)
print("Employee Details")
print("ID is",employee[0])
print("Name is",employee[1])
print("Department is",employee[2])
print("Salary is",employee[3])
'''

# 3. WAP to read product details from user like product name, price and quantity, store them in a tuple and calculate total bill.

name = input("Enter product name: ")
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))

bill = (name,price,qty)
amount = bill[1]*bill[2]

print("Bill Details:")
print(bill[0],"-> ",end=" ")
print("Price is",bill[1])
print("Total Amount:",amount)