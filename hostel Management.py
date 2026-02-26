hostel = {}
students = set()

print("Hostel Room Reservation System")

run = 1
while run == 1:
    print("\nA. Add rooms")
    print("B. Check in")
    print("C. Check out")
    print("D. Display rooms")
    print("E. Stop")

    option = input("Choose option: ").upper()

    if option == "A":
        n = int(input("Number of rooms to add: "))
        i = 0
        while i < n:
            r = input("Room number: ")
            if r not in hostel:
                hostel[r] = ""
            i = i + 1

    elif option == "B":
        sname = input("Student name: ").lower()
        rno = input("Room number: ")

        if sname in students:
            print("Student already allotted")
        elif rno not in hostel:
            print("Room not available")
        elif hostel[rno] != "":
            print("Room occupied")
        else:
            hostel[rno] = sname
            students.add(sname)
            print("Checked in successfully")

    elif option == "C":
        rno = input("Room number: ")

        if rno in hostel and hostel[rno] != "":
            students.remove(hostel[rno])
            hostel[rno] = ""
            print("Checked out successfully")
        else:
            print("Invalid room or already empty")

    elif option == "D":
        for key, value in hostel.items():
            if value == "":
                print(key, "-> Empty")
            else:
                print(key, "->", value)

    elif option == "E":
        run = 0

    else:
        print("Wrong option")