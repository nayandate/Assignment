def generate_bill():
    patient_id = input("Enter Patient ID: ").strip()
    consultation_charges = float(input("Enter Consultation Charges: "))
    medicine_cost = float(input("Enter Medicine Cost: "))
    test_charges = float(input("Enter Test Charges: "))
    total_bill = consultation_charges + medicine_cost + test_charges

    print("\n========== Patient Bill ==========")
    print(f"Patient ID: {patient_id}")
    print(f"Consultation Charges: {consultation_charges:.2f}")
    print(f"Medicine Cost: {medicine_cost:.2f}")
    print(f"Test Charges: {test_charges:.2f}")
    print(f"Total Bill: {total_bill:.2f}")
    return total_bill
