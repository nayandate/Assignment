'''
3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000
'''

ai = int(input("Enter annual income: "))
if ai <= 250000 :
   print ("No Tax ")
elif ai <= 500000 :
   tax = (ai*5)//100 
   print("Tax Payable: ",tax)
elif ai <= 1000000 :
   tax = (ai*20//100) 
   print("Tax Payable: ",tax)
else :
   tax = (ai*30)//100 
   print("Tax Payable: ",tax)