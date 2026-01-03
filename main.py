# cli contact book

def load_contacts():
    contacts = {}
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found")
        return

    for name, phone in contacts.items():
        print(f"{name} : {phone}")


def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found")


def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved.")
            break
        else:
            print("Invalid choice.")


main()
