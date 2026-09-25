'''
Assignment 9: Product Inventory Management

A shopkeeper wants to manage the stock of a product.

Create a class Product with the following attributes:

Product ID

Product name

Price

Available quantity

Create the following methods:

add_stock() – Increase the available quantity.

sell_product() – Decrease the available quantity.

calculate_stock_value() – Calculate price × available quantity.

display_product() – Display product and stock details.

Sample operations:

Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3

Expected result:

Available Quantity: 12
Total Stock Value: 540000
'''

class Product:
    def add_stock(self):
        self.add = int(input("Increase Available Stock: "))

    def sell_product(self):
        self.remove = int(input("Remove Available Stock: "))

    def calculate_stock_value(self,price,quan):
        self.available = (quan + self.add - self.remove)
        self.value = self.available * price

    def display_product(self):
        print()
        print("Available Quantity:",self.available)
        print("Total Stock Value:",self.value)

id = int(input("Enter Product ID: "))
name = input("Enter Product name: ")
price = int(input("Enter Product price: "))
quan = int(input("Enter Available Product Quantity: "))

s1 = Product()
s1.add_stock()
s1.sell_product()
s1.calculate_stock_value(price,quan)
s1.display_product()