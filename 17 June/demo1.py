'''

Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

'''

amt = int(input("Enter total bill amount : "))
gst = int(input("Enter GST % : "))
sc = int(input("Enter service charge in % : "))
frd = int(input("Enter number of friends : "))


gstp = amt*gst/100
scp = amt*sc/100
fb = gstp+scp+amt
epp = fb/frd

print("Final Bill = ",fb)
print("Each Person Pays = ",epp)
