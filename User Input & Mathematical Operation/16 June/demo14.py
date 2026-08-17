'''
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
'''

cp = int(input("Cost Price = "))
sp = int(input("Selling Price = "))

profit = sp-cp
proper = (profit/cp)*100
print("Profit = ",profit)
print("Profit % = ",proper)