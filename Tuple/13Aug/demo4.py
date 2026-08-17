'''
QUESTION 4: ONLINE SHOPPING ORDERS
==================================
An online shopping company stores customer orders using NamedTuple.
Fields:
order_id, customer_name, product_name, amount
Requirements:
1. Read N order records from the user and store them in a list of NamedTuples.
---
2. Display all order details.
---
3. Find and display the order having the highest amount.
---
4. Calculate and display total sales.
---
5. Count the number of orders whose amount is greater than ₹10,000.
---
Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''

from collections import namedtuple
Order = namedtuple("patient",["order_id", "name", "product_name", "amount"])
n = int(input("Enter number of orders:"))
orders = []
for i in range(n):
    print("Enter Details:")
    id = input("Enter Patient ID:")
    name = input("Enter patient Name:")
    product = input("Enter product Name:")
    amount = int(input("Enter amount:"))
    p = Order(id,name,product,amount)
    orders.append(p)



print(orders)
print("details:")
for x in orders:
    print(x.order_id,x.name,x.product_name,x.amount)


print("Highest Value Order:")

max = 0
ans = []
for x in orders:
    if x.amount > max:
        max = x.amount
        ans.append(x)
print(ans[-1].order_id,ans[-1].name,ans[-1].product_name,ans[-1].amount)



print("Total Sales:")
sum = 0
for x in orders:
    sum += x.amount
print(sum)



count = 0
print("Orders Above ₹10,000:")
for x in orders:
    if x.amount > 10000:
        count+=1

print(count)