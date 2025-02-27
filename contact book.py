class Contact:
    def __init__(self):
        self.contacts = []  # Renamed for clarity

    def add(self):
        """Adds a contact number to the list."""
        try:
            number = int(input("Enter number to add: "))
            self.contacts.append(number)
            print(f"Number {number} added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def view(self):
        """Displays the contact list."""
        if self.contacts:
            print("Contact List:", self.contacts)
        else:
            print("No contacts available.")

    def search(self):
        """Searches for a contact number in the list."""
        try:
            number = int(input("Enter number to search: "))
            print("Found" if number in self.contacts else "Not found")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def update(self):
        """Updates a contact number if found."""
        try:
            old_number = int(input("Enter old number: "))
            new_number = int(input("Enter new number: "))
            if old_number in self.contacts:
                index = self.contacts.index(old_number)
                self.contacts[index] = new_number
                print(f"Number {old_number} updated to {new_number}.")
            else:
                print(f"Number {old_number} not found.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    def delete(self):
        """Deletes a contact number if it exists."""
        try:
            number = int(input("Enter number to delete: "))
            self.contacts.remove(number)
            print(f"Number {number} deleted successfully.")
        except ValueError:
            print("Invalid input or number not found.")


def menu():
    c = Contact()
    
    
    switch = {
        1: c.add,
        2: c.view,
        3: c.search,
        4: c.update,
        5: c.delete
    }

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 6:
                print("Exiting the program... Goodbye!")
                break
            action = switch.get(choice, lambda: print("Invalid choice, please try again!"))
            action()
        except ValueError:
            print("Please enter a valid number.")
menu()
