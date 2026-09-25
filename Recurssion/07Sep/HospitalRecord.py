'''
5. Hospital Record System (Search Digit)

A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found
'''

def check(id,digit):
    if id == 0:
        return False
    if id%10 == digit:
        return True
    return check(id//10,digit)
id = int(input("Enter Patient ID: "))
digit = int(input("Enter Digit: "))
check(id,digit)
if check(id,digit) == True:
    print("Digit Found")
else:
    print("Not Found")