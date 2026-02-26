entered_students = []
registered_students = []
def enter_student(name):
    entered_students.append(name)
    print(f"Student {name} has entered the event.")
def register_student(name):
    if name in entered_students:
        registered_students.append(name)
        print(f"Student {name} has been registered for the event.")
    else:
        print(f"Student {name} must enter the event before registering.")
def view_entered_students():
    if entered_students:
        print("Entered Students:")
        for student in entered_students:
            print(student)
    else:
        print("No students have entered the event yet.")
def view_registered_students():
    if registered_students:
        print("Registered Students:")
        for student in registered_students:
            print(student)
    else:
        print("No students have registered for the event yet.")
while True:
    print("\nEvent Management Menu:")
    print("1. Enter Student")
    print("2. Register Student")
    print("3. View Entered Students")
    print("4. View Registered Students")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter student name: ")
        enter_student(name)
    elif choice == '2':
        name = input("Enter student name to register: ")
        register_student(name)
    elif choice == '3':
        view_entered_students()
    elif choice == '4':
        view_registered_students()
    elif choice == '5':
        print("Exiting the event management system.")
        break
    else:
        print("Invalid choice. Please select a valid option.")