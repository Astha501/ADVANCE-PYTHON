class ParkingSlot:
    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.is_occupied = False
        self.vehicle_number = None

    def park_vehicle(self, vehicle_number):
        if not self.is_occupied:
            self.is_occupied = True
            self.vehicle_number = vehicle_number
            print(f"Vehicle {vehicle_number} parked in Slot {self.slot_number}.")
        else:
            print(f"Slot {self.slot_number} is already occupied.")

    def remove_vehicle(self):
        if self.is_occupied:
            print(f"Vehicle {self.vehicle_number} removed from Slot {self.slot_number}.")
            self.is_occupied = False
            self.vehicle_number = None
        else:
            print("Slot is already empty.")

    def display_status(self):
        if self.is_occupied:
            print(f"Slot {self.slot_number} → Occupied by {self.vehicle_number}")
        else:
            print(f"Slot {self.slot_number} → Available")



class ParkingLot:
    def __init__(self, total_slots):
        self.slots = []
        for i in range(1, total_slots + 1):
            self.slots.append(ParkingSlot(i))

    def show_slots(self):
        print("\nParking Slot Status:")
        for slot in self.slots:
            slot.display_status()

    def park(self, slot_number, vehicle_number):
        if 1 <= slot_number <= len(self.slots):
            self.slots[slot_number - 1].park_vehicle(vehicle_number)
        else:
            print("Invalid slot number.")

    def exit(self, slot_number):
        if 1 <= slot_number <= len(self.slots):
            self.slots[slot_number - 1].remove_vehicle()
        else:
            print("Invalid slot number.")


def main():
    parking = ParkingLot(5)  # Create parking lot with 5 slots

    while True:
        print("\n--- Parking Management System ---")
        print("1. Show Slots")
        print("2. Park Vehicle")
        print("3. Remove Vehicle")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            parking.show_slots()

        elif choice == '2':
            slot_no = int(input("Enter Slot Number: "))
            vehicle_no = input("Enter Vehicle Number: ")
            parking.park(slot_no, vehicle_no)

        elif choice == '3':
            slot_no = int(input("Enter Slot Number to Remove Vehicle: "))
            parking.exit(slot_no)

        elif choice == '4':
            print("Thank you for using Parking System!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()