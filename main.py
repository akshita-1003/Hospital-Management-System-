from operations_manager import OperationsManager

manager = OperationsManager()

while True:

    print("\n")
    print("===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. Show Patients")
    print("3. Search Patient")
    print("4. Remove Patient")
    print("5. Get Next Patient")
    print("6. Book Appointment")
    print("7. Show Appointments")
    print("8. Hospital Report")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_patient()

    elif choice == "2":
        manager.show_patients()

    elif choice == "3":
        manager.search_patient()

    elif choice == "4":
        manager.remove_patient()

    elif choice == "5":
        manager.next_patient()

    elif choice == "6":
        manager.book_appointment()

    elif choice == "7":
        manager.show_appointments()

    elif choice == "8":
        manager.hospital_report()

    elif choice == "9":
        print("Thank You")
        break

    else:
        print("Invalid Choice")