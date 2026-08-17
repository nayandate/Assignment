'''
QUESTION 2: STUDENT RESULT PROCESSING
=====================================
A training institute wants to manage student records using NamedTuple.
Fields:
roll_no, name, course, marks

Requirements:
1. Read N student records from the user and store them in a list of NamedTuples.
---
2. Display all student details.
---
3. Find and display the topper of the class.
---
4. Count and display the number of students scoring above 80 marks.
---
5. Calculate and display the average marks.
---
6. Accept a course name from the user and display all students enrolled in that course.
---
Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
'''

from collections import namedtuple
Student = namedtuple("employee",["roll_no", "name", "course", "marks"])
n = int(input("Enter number of students:"))
students = []
for i in range(n):
    print("Enter Details:")
    rollno = int(input("Enter rollno:"))
    name = input("Enter Student Name:")
    course = input("Enter Course Name:")
    marks = int(input("Enter Student Makrs:"))
    stud = Student(rollno,name,course,marks)
    students.append(stud)

crse = input("Enter course:")

print(students)
print("details:")
for x in students:
    print(x.roll_no,x.name,x.course,x.marks)


print("Topper:")
max = 0
ans = []
for x in students:
    if x.marks > max:
        max = x.marks
        ans.append(x)
print(ans[-1].roll_no,ans[-1].name,ans[-1].course,ans[-1].marks)

ans.clear()
count = 0
print("Students Above 80:")

for x in students:
    if x.marks > 80:
        count+=1
print(count)

print("Average Marks:")
avg = 0
for x in students:
    avg += x.marks
      
print(avg/len(students))



print("Students in",crse,"Course:")
for x in students:
    if x.course == crse:
        print(x.roll_no,x.name,x.course,x.marks)