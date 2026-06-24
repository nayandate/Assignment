'''
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''

dist = int(input("Distance = "))
mil = int(input("Mileage = "))
pet = int(input("Petrol Price = "))

cost = (dist//mil)*pet
print("Cost = ",cost)