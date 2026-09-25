from models.employee import Employee

def display_employees(title, employees):
    print(title)
    for employee in employees:
        print(employee)
    print()


def main():
    employees = []

    for number in range(5):
        employee_id, name, salary, department = input(
            f"Enter details for employee {number + 1}: "
        ).split()
        employees.append(
            Employee(int(employee_id), name, int(salary), department)
        )

    display_employees("All Employees:", employees)
    display_employees(
        "Employees with salary greater than 40000:",
        [employee for employee in employees if employee.salary > 40000],
    )
    display_employees(
        "Employees from IT Department:",
        [employee for employee in employees if employee.department == "IT"],
    )

    highest_salary_employee = max(employees, key=lambda employee: employee.salary)
    print("Highest Salary Employee:")
    print(highest_salary_employee)
    print()

    total_salary = sum(employee.salary for employee in employees)
    print("Total Salary:")
    print(total_salary)
    print()

    average_salary = total_salary / len(employees)
    print("Average Salary:")
    print(f"{average_salary:g}")


if __name__ == "__main__":
    main()
