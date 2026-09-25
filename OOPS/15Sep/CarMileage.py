'''
Assignment 8: Car Mileage Calculator

A car owner wants to calculate the mileage and fuel cost of a journey.

Create a class Car with the following attributes:

Car brand

Car model

Distance travelled in km

Fuel consumed in litres

Petrol price per litre

Create the following methods:

calculate_mileage() – Calculate kilometres per litre.

calculate_fuel_cost() – Calculate total fuel cost.

display_trip_details() – Display car and journey details.

Formulas:

Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price

Sample data:

Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litrese_mileage
Petrol Price: 105
'''

class Car:
    def calculate(self,dis,fuel):
        self.dis=dis 
        self.fuel=fuel
        self.mileage = dis/fuel

    def calculate_fuel_cost(self,price):
        self.price = price
        self.fuel_cost = self.fuel * price

    def display_trip_details(self,brand,model):
        print()
        print("Car Brand: ",brand)
        print("Car Model: ",model)
        print("Distance travelled in km: ",self.dis)
        print("Fuel consumed in litres: ",self.fuel)
        print("Petrol price per litre: ",self.price)
        print("Mileage: ",self.mileage)
        print("Fuel Cost: ",self.fuel_cost)
        
brand = input("Car Brand: ")
model  = input("Car Model: ")
dis = int(input("Distance travelled in km: "))
fuel = int(input("Fuel consumed in litres: "))
price = int(input("Petrol price per litre: "))

s1 = Car()
s1.calculate(dis,fuel)
s1.calculate_fuel_cost(price)
s1.display_trip_details(brand,model)