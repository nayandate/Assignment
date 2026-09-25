'''
Assignment 1 — Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days
'''

from datetime import timedelta, datetime
dob = input("Enter DOB (DD-MM-YYYY): ")
dob = datetime.strptime(dob,"%d-%m-%Y")
today = datetime.now()
print("Age:", age, "years")
print("Completed Months:", months, "months")
print("Total Days Lived:", total_days, "days")
print("Next Birthday:", next_birthday.strftime("%d-%m-%Y"))
print("Days Remaining:", days_remaining, "days")