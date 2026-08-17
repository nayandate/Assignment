# 1. WAP to store account detail in namedtuple.

'''
from collections import namedtuple
Account = namedtuple("Acc",["Accno","Holdername","Balance"])

Accno = int(input("Enter account number: "))
Name = input("Enter account holder name: ")
Balance = float(input("Enter account balance: "))

acc = Account(Accno,Name,Balance)
print("Account Details: ")
print()
print("Account Number: ",acc.Accno)
print("Account Holder Name: ",acc.Holdername)
print("Account Balance: ",acc.Balance)
'''

# 2. WAP to store student detail in namedtuple

from collections import namedtuple
Student = namedtuple("Student",["Name","Rollno","Marks"])

n = int(input("Enter no. of students: "))
students = []
for i in range(n):
     print("Enter details of Student",i+1,":")
     Name = input("Enter Name of student: ")
     Rollno = int(input("Enter roll number: "))
     Marks = float(input("Enter marks: "))
     S = Student(Name,Rollno,Marks)
     students.append(S)

print()
print("Student Details: ")

for ch in students:
     print(ch.Rollno,"->",ch.Name,"and",ch.Marks)
