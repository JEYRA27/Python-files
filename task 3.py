import csv
import os

CONTACTS_FILE = "contacts.csv"

def load_contacts():
    """Load contacts from the CSV file."""
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    return contacts

def save_contacts(contacts):
    """Save contacts to the CSV file."""
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        fieldnames = ['name', 'phone', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

def add_contact(contacts):
    """Add a new contact to the contact list."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print(f"Contact {name} added.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    """Edit an existing contact."""
    view_contacts(contacts)
    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave field blank to keep the current value.")
            name = input(f"Enter new name (current: {contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"Enter new phone (current: {contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"Enter new email (current: {contacts[index]['email']}): ") or contacts[index]['email']
            contacts[index] = {'name': name, 'phone': phone, 'email': email}
            save_contacts(contacts)
            print("Contact updated.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact(contacts):
    """Delete a contact from the list."""
    view_contacts(contacts)
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact {deleted_contact['name']} deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def main():
    """Main function to run the contact management system."""
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
