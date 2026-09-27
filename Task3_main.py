import json
from pathlib import Path

FILE_NAME = "contacts.json"


def load_contacts():
    path = Path(FILE_NAME)
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n=== Contact List ===")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")


def delete_contact(contacts):
    if not contacts:
        print("No contacts to delete.")
        return

    view_contacts(contacts)

    try:
        number = int(input("Enter contact number to delete: "))
        if 1 <= number <= len(contacts):
            removed = contacts.pop(number - 1)
            save_contacts(contacts)
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    contacts = load_contacts()

    while True:
        print("\n=== Simple Contact Management System ===")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete contact")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
