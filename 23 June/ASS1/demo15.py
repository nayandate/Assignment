'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
'''

vhcl = input("Enter vehicle type(Car, Bus, Bike): ").lower()
chg = int(input("Enter hours packed: "))

if vhcl == "bike":
    if chg <=5:
        print("Total Parking Fee: ₹",chg*10)
    else:
        print("Total Parking Fee: ₹",chg*10+100)
elif vhcl == "car":
    if chg <=5:
        print("Total Parking Fee: ₹",chg*20)
    else:
        print("Total Parking Fee: ₹",chg*20+100)
elif vhcl == bike:
    if chg <=5:
        print("Total Parking Fee: ₹",chg*50)
    else:
        print("Total Parking Fee: ₹",chg*50+100)
else:
    print("Wrong vehicle type")