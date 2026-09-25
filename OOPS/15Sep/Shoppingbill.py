'''
Assignment 5: Shopping Bill Calculator

A retail shop wants to calculate the total bill for a customer.

Create a class ShoppingBill with the following attributes:

Product name

Product price

Quantity

Discount percentage

GST percentage

Create the following methods:

calculate_subtotal() - Calculate price * quantity.

calculate_discount() - Calculate the discount amount.

calculate_gst() - Calculate GST on the discounted amount.

calculate_final_bill() - Calculate the final payable amount.

display_bill() - Display the complete bill details.

Formula:

Subtotal = Price * Quantity
Discounted Amount = Subtotal - Discount Percentage / 100
GST = Discounted Amount * GST Percentage / 100
Final Bill = Discounted Amount + GST
'''

class ShoppingBill:
    def calculate_subtotal(self,price,quan):
        self.price = price
        self.quan = quan
        self.sub = price * quan

    def calculate_discount(self,dis_per):
        self.discount = self.sub - self.sub*(dis_per/100)

    def calculate_gst(self,gst_per):
        self.gst = self.discount + self.discount*(gst_per/100)

    def calculate_final_bill(self,name):
        self.name = name
        self.bill = self.discount + self.gst
        print()
        print("Product Name:",self.name)
        print("Product Price:",self.price)
        print("Product Quantity:",self.quan)
        print("Product Subtotal:",self.sub)
        print("Product Price after Discount:",self.discount)
        print("Total Bill:",self.gst)

name = input("Enter Product name: ")
price = int(input("Enter Product price: "))
quan = int(input("Enter Product Quantity: "))
dis_per = float(input("Enter Discount percentage: "))
gst_per = float(input("Enter GST percentage: "))

s1 = ShoppingBill()

s1.calculate_subtotal(price,quan)
s1.calculate_discount(dis_per)
s1.calculate_gst(gst_per)
s1.calculate_final_bill(name)

