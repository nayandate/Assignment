'''
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
'''

amount = int(input("Enter Total Amount : "))
discount = (amount//10)
Final = amount - discount
print("Discount = ",discount)
print("Final = ",Final)

