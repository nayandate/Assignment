'''
====================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
'''

from collections import namedtuple
emp = namedtuple("employee", ["emp_id", "emp_name", "department", "salary"])
employees = []
n = int(input("Enter the number of employees: "))
for i in range(n):
    id = int(input("Enter EMP ID: "))
    name = input("Enter EMP name: ")
    dep = input("Enter department name: ")
    sal = int(input("Enter salary: "))
    Emp = emp(id, name, dep, sal)
    employees.append(Emp)
print("\nAll Employee Details:")
for e in employees:
    print(e.emp_id, e.emp_name, e.department, e.salary)

highest = employees[0]
for e in employees:
    if e.salary > highest.salary:
        highest = e
print("\nHighest Salary Employee:")
print(highest.emp_id, highest.emp_name, highest.department, highest.salary)

lowest = employees[0]
for e in employees:
    if e.salary < lowest.salary:
        lowest = e
print("\nLowest Salary Employee:")
print(lowest.emp_id, lowest.emp_name, lowest.department, lowest.salary)

total = 0
for e in employees:
    total = total + e.salary
average = total / n
print("\nAverage Salary:")
print(average)

c = input("\nEnter the department name: ")
for e in employees:
    if e.department == c:
        print(e.emp_id, e.emp_name, e.department, e.salary)