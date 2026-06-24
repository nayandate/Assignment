'''
Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
'''

amount = int(input("Amount = "))

hun = amount // 100
fif = (amount % 100) // 50
ten = ((amount % 100) % 50) // 10
print("₹100 = ",hun)
print("₹50 = ",fif)
print("₹10 = ",ten)