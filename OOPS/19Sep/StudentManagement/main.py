from Models import Student

def display_student(self):
    print(self.roll_no,self.name,self.marks)

def main():
    students = []

    for i in range(1, 6):
        print(f"\nEnter details of Student {i}:")
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        st = Student(roll_no, name, marks)
        students.append(st)

    print("\nAll Students:")
    for student in students:
        display_student(student)

    print("\nStudents having marks greater than 60:")
    for student in students:
        if student.marks > 60:
            display_student(student)

    highest_student = max(students, key=lambda student: student.marks)
    print("\nHighest Marks:")
    display_student(highest_student)

    average_marks = sum(student.marks for student in students) / len(students)
    print("\nAverage Marks:")
    print(average_marks)


if __name__ == "__main__":
    main()

