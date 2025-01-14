# Dictionary to store reservations
reservations = {}

# Function to make a reservation
def make_reservation():
    print("\nEnter the following details to book a reservation:")
    name = input("Name: ")
    date = input("Date (DD/MM/YYYY): ")
    total_members = input("Total Members: ")
    phone_number = input("Phone Number: ")

    reservation_id = len(reservations) + 1  # Auto-generate reservation ID
    reservations[reservation_id] = {
        "Name": name,
        "Date": date,
        "Total Members": total_members,
        "Phone Number": phone_number
    }

    print(f"\nReservation successful! Your reservation ID is {reservation_id}\n")

# Function to view all reservations
def view_reservations():
    if reservations:
        print("\nCurrent Reservations:")
        for res_id, details in reservations.items():
            print(f"\nReservation ID: {res_id}")
            for key, value in details.items():
                print(f"{key}: {value}")
            print("-" * 30)  # Line separator between reservations
    else:
        print("\nNo reservations found.\n")

# Function to update a reservation
def update_reservation():
    if reservations:
        reservation_id = int(input("\nEnter the Reservation ID to update: "))
        if reservation_id in reservations:
            print("\nEnter the new details (leave blank to keep current information):")
            name = input(f"Name [{reservations[reservation_id]['Name']}]: ") or reservations[reservation_id]['Name']
            date = input(f"Date (DD/MM/YYYY) [{reservations[reservation_id]['Date']}]: ") or reservations[reservation_id]['Date']
            total_members = input(f"Total Members [{reservations[reservation_id]['Total Members']}]: ") or reservations[reservation_id]['Total Members']
            phone_number = input(f"Phone Number [{reservations[reservation_id]['Phone Number']}]: ") or reservations[reservation_id]['Phone Number']

            reservations[reservation_id] = {
                "Name": name,
                "Date": date,
                "Total Members": total_members,
                "Phone Number": phone_number
            }

            print(f"\nReservation ID {reservation_id} has been updated.\n")
        else:
            print("Invalid Reservation ID.\n")
    else:
        print("No reservations to update.\n")

# Function to delete a reservation
def delete_reservation():
    if reservations:
        reservation_id = int(input("\nEnter the Reservation ID to delete: "))
        if reservation_id in reservations:
            del reservations[reservation_id]
            print(f"Reservation ID {reservation_id} has been deleted.\n")
        else:
            print("Invalid Reservation ID.\n")
    else:
        print("No reservations to delete.\n")

# Main function to display options
def main_menu():
    while True:
        print("\n--- Online Reservation System ---")
        print("1. Make a Reservation")
        print("2. View Reservations")
        print("3. Update a Reservation")
        print("4. Delete a Reservation")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            make_reservation()
        elif choice == "2":
            view_reservations()
        elif choice == "3":
            update_reservation()
        elif choice == "4":
            delete_reservation()
        else:
            print("Invalid choice. Please try again.\n")

# Running the system
if __name__ == "__main__":
    main_menu()