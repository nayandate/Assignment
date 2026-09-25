doctors = []


def add_doctor():
    doctor = {
        "Doctor ID": input("Enter Doctor ID: ").strip(),
        "Doctor Name": input("Enter Doctor Name: ").strip(),
        "Specialization": input("Enter Specialization: ").strip(),
        "Experience": input("Enter Experience: ").strip(),
        "Consultation Fees": input("Enter Consultation Fees: ").strip(),
    }
    doctors.append(doctor)
    print("Doctor added successfully.")
    return doctor


def display_doctors():
    if not doctors:
        print("No doctors registered.")
        return

    for doctor in doctors:
        for field, value in doctor.items():
            print(f"{field}: {value}")
        print("-" * 30)
