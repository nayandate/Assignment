appointments = []

def book_appointment():
    appointment = {
        "Appointment ID": input("Enter Appointment ID: ").strip(),
        "Patient ID": input("Enter Patient ID: ").strip(),
        "Doctor ID": input("Enter Doctor ID: ").strip(),
        "Appointment Date": input("Enter Appointment Date: ").strip(),
        "Appointment Time": input("Enter Appointment Time: ").strip(),
    }
    appointments.append(appointment)
    print("Appointment booked successfully.")
    return appointment


def show_appointments():
    if not appointments:
        print("No appointments booked.")
        return

    for appointment in appointments:
        for field, value in appointment.items():
            print(f"{field}: {value}")
        print("-" * 30)
