'''
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System
'''

Patient = {}
while True:
    print()
    print("=====================================")
    print("HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("=====================================")

    print('''
1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit''')

    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            n = int(input("How many patient you want to add?   "))
            for i in range(n):
                print()
                Patient_ID = int(input(f"Enter Patient {i+1} ID: "))
                if Patient_ID not in Patient:
                    Patient_Name = (input("Enter Patient Name: "))
                    Patient_Age = int(input("Enter Patient Age: "))
                    Patient_Gender = input("Enter Patient Gender: ")
                    Patient_Disease = input("Enter Patient Disease: ")
                    Doctor_Name = (input("Enter Patient Doctor Name: "))
                    Patient[Patient_ID] = {"Name" : Patient_Name , "Age" : Patient_Age, "Gender" : Patient_Gender, "Disease":Patient_Disease,"Doctor Name":Doctor_Name}
                else:
                    print("Patient already exist with same Patient ID.")
            
        case 2:
            print()
            search = int(input("Enter Patient ID to find: "))
            print()
            if search in Patient:
                for k,v in Patient[search].items():
                    print(k,":",v)
            else:
                print("Patient Record Not Found")

        
        case 3:
            print()
            update_id = int(input("Enter Patient ID to update disease: "))
            print()
            if update_id in Patient:
                print("Patient Name :",Patient[update_id]["Name"])
                print("Old Disease :",Patient[update_id]["Disease"])
                update_disease = input("Enter New Disease : ")
                Patient[update_id]["Disease"] = update_disease
                print("Disease Updated Successfully")
                
            else:
                print("Patient ID Not Found")

        # case 4:
        # case 5:
        # case 6:
        # case 7:
        # case 8:
        # case 9:
        
        case 10:
            print("Thank You For Using Hospital Patient Management System.........")
            break