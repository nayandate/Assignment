import uuid

print("1. Generate UUID")
print("2. Generate UUID from name")

choice = int(input("Enter your choice: "))

if choice == 1:
    # Random unique UUID generate karega
    id = uuid.uuid4()
    print("Your UUID is:", id)

elif choice == 2:
    # Name ke basis par UUID generate karega
    id = uuid.uuid5(uuid.NAMESPACE_DNS, "nayan.com")
    print("Your UUID is:", id)

else:
    print("Invalid choice")