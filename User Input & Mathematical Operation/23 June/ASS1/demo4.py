'''
4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050
'''

pa = int(input("Enter purchase amount: "))
if pa > 5000:
   disc = pa - (pa*20)/100
   print ("Final Amount: ",disc)
elif pa >= 2000 :
   disc = pa - (pa*10)/100
   print("Final Amount: ",disc)
else :
   disc = pa - (pa*5)/100
   print("Final Amount: ",disc)
