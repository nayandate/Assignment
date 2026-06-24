'''
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
'''

dis = int(input("Enter distance : "))
mil,pp = map(int,input("Enter Mileage and Petrol price : ").split())

pu = (dis/mil)
print(f"Petrol Used = {pu} litres")

tc = pp*pu
print(f"Total Cost = {tc}")
