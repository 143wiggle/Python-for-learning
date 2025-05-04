contact_book = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contact_book[name] = phone
    print(f"Contact for {name} added successfully!")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact_book:
        print(f"{name}: {contact_book[name]}")
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contact_book:
        new_phone = input("Enter new phone number: ")
        contact_book[name] = new_phone
        print(f"Contact for {name} updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print("Contact not found!")

def display_contacts():
    if contact_book:
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available!")

def main():
    while True:
        print("\n1. Add Contact\n2. Search Contact\n3. Update Contact\n4. Delete Contact\n5. Display Contacts\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
