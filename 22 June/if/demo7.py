'''
7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable
'''

slr = int(input("Enter Salary : "))

if slr >= 30000 :
    print ("PF applicable")

if slr >= 50000 :
    print ("Bonus applicable")