from string_operations.substring import print_substrings
from list_operations.subarray import minimum_subarray


while True:
    print("\n========== MENU ==========")
    print("1. Print All Substrings")
    print("2. Minimum Size Subarray Sum")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        string = input("Enter a string: ")
        print("\nAll substrings are:")
        print_substrings(string)

    elif choice == 2:
        n = int(input("Enter number of elements: "))

        numbers = []
        print("Enter elements:")

        for i in range(n):
            numbers.append(int(input()))

        target = int(input("Enter target: "))

        result = minimum_subarray(numbers, target)

        print("\nList:", numbers)
        print("Target:", target)
        print("\nMinimum size subarray:", result)

    elif choice == 3:
        print("Thank you for using the application.")
        break

    else:
        print("Invalid choice. Please enter a valid choice.")