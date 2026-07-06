'''
2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!
'''

print("\n1 → Enter Basic Salary \n2 → Calculate HRA (20%) and DA (10%) \n3 → Calculate Net Salary \n4 → Tax Deduction \n5 → Display Salary Slip \n6 → Exit")

bs = 0
hra = None
da = None
fs = None
ns = None
tax = None
while True:
  ch = int(input("Enter your choice : "))
  match ch:
   case 1:
          bs = input("Enter Basic Salary : ")
          if bs=="":
               print("Enter Salary first")
          else:
             bs = int(bs)
             if bs<=0:
                print("Salary can not be 0 or less")
             else:
                print("Basic Salary recorded successfully")
		

   case 2:
          if bs<=0:
               print("Enter Salary first")
          else:
               hra = bs*20//100
               da = bs*10//100
               print("HRA = ",hra)
               print("DA = ",da)
 
   case 3:
       if bs<=0:
         print("Enter Salary first")
       else:
         hra = bs*20//100
         da = bs*10//100
         ns = bs+hra+da
         print("Net Salary (before tax) : ",ns)

   case 4:
      if bs<=0:
         print("Enter Salary first")
      else:
         if ns>50000:
             tax = ns*10//100
         else:
             tax = ns*5//100
         print("Tax : ",tax)

   case 5:
     if bs<=0:
         print("Enter Salary first")
     else:
         hra = bs*20//100
         da = bs*10//100
         ns = bs+hra+da
         if ns>50000:
             tax = ns*10//100
         else:
             tax = ns*5//100
         print("Tax : ",tax)
         print("----- Salary Slip -----")
         print("Basic Salary:",bs)
         print("HRA:",hra)
         print("DA:",da)
         print("Net Salary:",ns)
         print("Tax:",tax)
         fs = ns - tax
         print("Final Salary:",fs)

   case 6:
         print("Exiting program... Thank you!")
         break

   case __:
         print("Invalid choice. Please try again.")