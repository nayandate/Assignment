'''
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================
A hospital stores patient records for daily monitoring.
Fields:
patient_id, patient_name, age, disease

Requirements:
1. Read N patient records from the user and store them in a list of NamedTuples.
---
2. Display all patient details.
---
3. Display patients whose age is above 60 years.
---
4. Search for a patient using Patient ID.
---
5. Count the number of patients suffering from a particular disease.
---
Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
'''


from collections import namedtuple
Patient = namedtuple("patient",["patient_id", "name", "age", "disease"])
n = int(input("Enter number of Patients:"))
patient = []
for i in range(n):
    print("Enter Details:")
    id = input("Enter Patient ID:")
    name = input("Enter patient Name:")
    age = int(input("Enter patient age:"))
    disease = input("Enter patient Disease:")
    p = Patient(id,name,age,disease)
    patient.append(p)

findID = input("Enter Patient ID:")
findDis = input("Enter Disease ID:")

print(patient)
print("details:")
for x in patient:
    print(x.patient_id,x.name,x.age,x.disease)


print("Patient Found:")

for x in patient:
    if x.patient_id == findID:
        print(x.patient_id,x.name,x.age,x.disease)



print("Patients Above 60:")

for x in patient:
    if x.age > 60:
        print(x.patient_id,x.name,x.age,x.disease)



count = 0
print("Patients with",findDis,":")
for x in patient:
    if x.disease == findDis:
        count+=1

print(count)