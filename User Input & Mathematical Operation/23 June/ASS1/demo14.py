'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''

cc = input("Enter course category(Programming, Design, Marketing): ").lower()
ut = input("Enter user type(Student, Working, Others): ").lower()

if cc == "programming":
     if ut == "student":
          print("Final Course Fee: ₹4000")
     else:
         if ut == "working professional":
             print("Final Course Fee: ₹4500")
         else:
             print("Final Course Fee(No discount): ₹5000")
elif cc == "design":
     if ut == "student":
          print("Final Course Fee: ₹3200")
     else:
         if ut == "working professional":
             print("Final Course Fee: ₹3600")
         else:
             print("Final Course Fee(No discount): ₹4000")
else :
     if ut == "student":
          print("Final Course Fee: ₹2400")
     else:
         if ut == "working professional":
             print("Final Course Fee: ₹2700")
         else:
             print("Final Course Fee(No discount): ₹3000")