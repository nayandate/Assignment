'''
2. Hospital Management System - Oldest Patient

A hospital wants to give priority to the oldest patient during a free health check-up camp. The patient details are stored as tuples containing the patient's name and age.

As a Python developer, write a program to identify the oldest patient using the reduce() function with a lambda expression.

Input
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]
Expected Output
Oldest Patient: Kiran
'''

from functools import reduce
patients = []
n = int(input("Enter total patients: "))
for i in range(n):
    print()
    name = input(f"Enter name of {i+1} patient: ")
    age = int(input(f"Enter age of {i+1} patient: "))
    pat=(name,age)
    patients.append(pat)
print("Patients:",patients)

result = reduce(lambda x,y: y if x[1]<y[1] else x,patients)
print(result[0])