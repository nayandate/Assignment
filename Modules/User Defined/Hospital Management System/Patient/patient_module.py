patients = []


def add_patient():
    patient = {
        "Patient ID": input("Enter Patient ID: ").strip(),
        "Patient Name": input("Enter Patient Name: ").strip(),
        "Age": input("Enter Age: ").strip(),
        "Gender": input("Enter Gender: ").strip(),
        "Disease": input("Enter Disease: ").strip(),
        "Mobile Number": input("Enter Mobile Number: ").strip(),
    }
    patients.append(patient)
    print("Patient added successfully.")
    return patient


def display_patients():
    if not patients:
        print("No patients registered.")
        return

    for patient in patients:
        for field, value in patient.items():
            print(f"{field}: {value}")
        print("-" * 30)


def search_patient():
    patient_id = input("Enter Patient ID to search: ").strip()
    for patient in patients:
        if patient["Patient ID"] == patient_id:
            for field, value in patient.items():
                print(f"{field}: {value}")
            return patient

    print("Patient not found.")
    return None
