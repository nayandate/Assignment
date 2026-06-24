'''
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
'''

sal = int(input("Enter salary: "))
rat = int(input("Enter rating: "))

if rat==5 :
   if sal<20000:
        print("Revised Salary",(sal*25//100+sal+2000))
   else:
        print("Revised Salary",(sal*25//100+sal))
elif rat==4 :
   if sal<20000:
        print("Revised Salary",(sal*20//100+sal+2000))
   else:
        print("Revised Salary",(sal*20//100+sal))
elif rat==3 :
    print("Revised Salary",(sal*10//100+sal))
elif rat==2 :
    print("Revised Salary",(sal*5//100+sal))
else:
    print("No Hike ",sal)