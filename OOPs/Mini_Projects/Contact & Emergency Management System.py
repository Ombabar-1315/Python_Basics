class ContactNotFound(Exception):
    pass


class Contact:
    total_contacts = 0

    def __init__(self, name, phone, email, category):
        self.name = name
        self.category = category

        if not Contact.validate_phone(phone):
            raise ValueError("Enter a valid phone number.")

        if "@" not in email:
            raise ValueError("Enter a valid email.")

        self.__phone = phone
        self.email = email

        Contact.total_contacts += 1

    @property
    def phone(self):
        return self.__phone

    @staticmethod
    def validate_phone(phone):
        if len(phone) == 10 and phone.isdigit():
            return True
        return False

    def update_phone(self, phone):
        if Contact.validate_phone(phone):
            self.__phone = phone
            print("Phone updated successfully.")
        else:
            print("Enter a valid phone number.")

    def update_email(self, new_email):
        if "@" in new_email:
            self.email = new_email
            print("Email updated successfully.")
        else:
            print("Invalid email.")

    @classmethod
    def show_total_contacts(cls):
        return cls.total_contacts

    def display_contact(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Category:", self.category)


contacts = []


def add_contact():
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        category = input("Enter Category: ")

        contact = Contact(name, phone, email, category)
        contacts.append(contact)

        print("Contact added successfully.")

    except ValueError as e:
        print(e)


def display_all_contacts():
    try:
        if not contacts:
            raise ContactNotFound("No contacts found.")

        for contact in contacts:
            contact.display_contact()
            print("--------------------------")

    except ContactNotFound as e:
        print(e)


def search_contact():
    search_name = input("Enter name to search: ")

    try:
        found = False

        for contact in contacts:
            if search_name == contact.name:
                found = True

                print("\nContact Found:")
                contact.display_contact()

                break

        if not found:
            raise ContactNotFound("Contact not found.")

    except ContactNotFound as e:
        print(e)


def update_contact():
    contact_name = input("Enter Contact Name: ")

    try:
        found = False

        for contact in contacts:
            if contact_name == contact.name:
                found = True

                while True:
                    print("\n1. Update Phone")
                    print("2. Update Email")
                    print("3. Cancel")

                    try:
                        choice = int(input("Enter Choice: "))
                    except ValueError:
                        print("Enter a number between 1 and 3.")
                        continue

                    if choice == 1:
                        new_number = input("Enter New Number: ")
                        contact.update_phone(new_number)
                        break

                    elif choice == 2:
                        new_email = input("Enter New Email: ")
                        contact.update_email(new_email)
                        break

                    elif choice == 3:
                        print("Update cancelled.")
                        break

                    else:
                        print("Invalid choice. Try again.")

                break

        if not found:
            raise ContactNotFound("Contact not found.")

    except ContactNotFound as e:
        print(e)


def delete_contact():
    contact_name = input("Enter Contact Name: ")

    try:
        found = False

        for contact in contacts:
            if contact_name == contact.name:
                found = True

                contacts.remove(contact)

                # Decrease current contact count
                Contact.total_contacts -= 1

                print(f"{contact_name} deleted successfully.")
                break

        if not found:
            raise ContactNotFound("Contact not found for deletion.")

    except ContactNotFound as e:
        print(e)


print("======================================")
print("     CONTACT MANAGEMENT SYSTEM")
print("======================================")


while True:

    print()
    print("1. Add Contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Show Total Contacts")
    print("7. Exit")

    try:
        choice = int(input("Enter Choice: "))

    except ValueError:
        print("Enter a valid number from 1 to 7.")
        continue

    if choice == 1:
        add_contact()

    elif choice == 2:
        display_all_contacts()

    elif choice == 3:
        search_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        print("Total Contacts:", Contact.show_total_contacts())

    elif choice == 7:
        print("Thank you for using Contact Management System.")
        break

    else:
        print("Invalid Choice. Try Again.")