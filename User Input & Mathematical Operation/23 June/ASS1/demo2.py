'''
2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C
'''

mark = int(input("Enter marks: "))
grd = "Grade A" if mark>=90 else "Grade B" if mark>=75 else "Grade C" if mark>=60 else "Grade D" if mark>=50 else "Fail" 

print(grd)