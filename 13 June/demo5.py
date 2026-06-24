#Your shopping cart total doesn’t include tax. A 12% GST is applied.

cart=float(input("Enter the total amount"))
tax=cart*(12/100)
total=cart+tax
print("Cart=₹{}\nTax=₹{}\nTotal=₹{}".format(cart,tax,total))
