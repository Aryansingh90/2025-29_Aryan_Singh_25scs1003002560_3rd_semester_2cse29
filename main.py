import json
from pathlib import Path

FILE = Path("contacts.json")

def load_contacts():
    if FILE.exists():
        try:
            return json.loads(FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []
    return []

def save_contacts(contacts):
    FILE.write_text(json.dumps(contacts, indent=4), encoding="utf-8")

def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

def search_contact(contacts):
    q = input("Enter name to search: ").strip().lower()
    matches = [c for c in contacts if q in c["name"].lower()]
    if not matches:
        print("No matching contacts found.")
    for c in matches:
        print(f"{c['name']} | {c['phone']} | {c['email']}")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        n = int(input("Enter contact number to delete: "))
        if 1 <= n <= len(contacts):
            removed = contacts.pop(n - 1)
            save_contacts(contacts)
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1": add_contact(contacts)
        elif choice == "2": view_contacts(contacts)
        elif choice == "3": search_contact(contacts)
        elif choice == "4": delete_contact(contacts)
        elif choice == "5": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
