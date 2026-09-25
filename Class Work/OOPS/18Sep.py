class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display_name(self):
        print(f"Name: {self.name}")

    def display_marks(self):
        print(f"Marks: {self.marks}")

    def display(self):
        self.display_name() 
        self.display_marks() 
        return self

s1 = Student("Nayan",20)
print(s1.display())
