'''

Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

'''

mp = int(input("Enter Mobile Price : "))
dp = int(input("Down Payment : "))
r = int(input("Enter Interest Rate : "))
mnt = int(input("Enter number of months : "))

rm = mp-dp
print("Remaining Amount = ",rm)

intr = int((rm*r/100)+rm)
print("Total with interest = ",intr)

emi = intr/mnt
print("Monthly EMI = ",emi)

