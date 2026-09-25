from Models.employee import Employee
from Models.project import Project

employees = []
projects = []
print("Enter Details Of Employees: ")
for i in range(5):
    print()
    employee_id = int(input(f"Enter employee id of {i+1} Employee: "))
    employee_name = input(f"Enter employee name of {i+1} Employee: ")
    department = input(f"Enter department of {i+1} Employee: ")
    salary = int(input(f"Enter salary of {i+1} Employee: "))
    emp =  Employee(employee_id,employee_name,department,salary)
    employees.append(emp)

print("Enter Details Of Projects: ")
for i in range(5):
    print()
    project_id = int(input(f"Enter project id of {i+1} Project: "))
    project_name = input(f"Enter project name of {i+1} Project: ")
    employee_id = int(input(f"Enter employee id of {i+1} Project: "))
    project_cost = int(input(f"Enter Project cost of {i+1} Project: "))
    proj =  Project(project_id,project_name,employee_id,project_cost)
    projects.append(proj)

while True:
    print("""
========= MENU ==========
1. Display All Employees
2. Search Employee by ID
3. Display Employees by Department
4. Find Highest Paid Employee
5. Display Employee Projects
6. Find Highest Cost Project
7. Exit""")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            print()
            print("Employee Details")
            for emp in employees:
                print(emp.employee_id,emp.employee_name,emp.department,emp.salary)

        case 2:
            print()
            search_id = int(input("Enter Employee ID to search: "))
            for emp in employees:
                if emp.employee_id == search_id:
                    print("\nEmployee Details:")
                    print("ID:", emp.employee_id)
                    print("Name:", emp.employee_name)
                    print("Department:", emp.department)
                    print("Salary:", emp.salary)
                    break
            else:
                print("Employee Not Found")
                
        case 3:
            print()
            search_dep = input("Enter Department: ")

            print()
            x = 0
            for emp in employees:
                if emp.department.lower() == search_dep.lower():
                    print(emp.employee_id,emp.employee_name,emp.department,emp.salary)
                    x = 1

            if x == 0:
                print("No Employees Found..........")
                
        case 4:
            print()
            highest = employees[0]
            for employee in employees:
                if employee.salary > highest.salary:
                    highest = employee
    
            print("Highest Paid Employee:")
            print("ID:", highest.employee_id)
            print("Name:", highest.employee_name)
            print("Department:", highest.department)
            print("Salary:", highest.salary)

        case 5:
            print()
            search_id = int(input("Enter Employee ID: "))
            x = 0
            print("\nEmployee Projects:")
            
            for project in projects:
                if project.employee_id == search_id:
                    print(project.project_id,project.project_name,project.project_cost)
                    x=1
            if x == 0:
                print("No projects found")
            
        case 6:
            highest_project = projects[0]
            for project in projects:
                if project.project_cost > highest_project.project_cost:
                    highest_project = project
            employee_name = "Not Found"
            for employee in employees:
                if employee.employee_id == highest_project.employee_id:
                    employee_name = employee.employee_name
                    break
            print("\nHighest Cost Project:")
            print("Project:", highest_project.project_name)
            print("Cost:", highest_project.project_cost)
            print("Employee:", employee_name)

        case 7:
            print("Exiting the Program.......")
            break

        case _:
            print("Invalid Choice")
        
