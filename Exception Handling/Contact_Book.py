contacts = [{ "name":"om", "number":9226562031 }]

def add_contact():
    name = input("Enter Name: ")
    number = input("Enter Number: ")

    if not number.isdigit():
        raise ValueError("❌ Phone number must contain digits only.")

    if len(number) != 10:
        raise ValueError("❌ Phone number must be exactly 10 digits.")

    contacts.append({"name": name, "number": number})
    print("Contact Added Successfully!")

class ContactNotFound(Exception):
    pass

def search_contact(contacts):
    name = input("Enter Name to Search: ")
    print()
    for con in contacts:
        if name == con["name"]:
            
            print("Name: ",con["name"])
            print("Phone: ",con["number"])
            return  
    raise ContactNotFound("Contact is Not Found.")

def delete_contact(contacts):
    name = input("Enter Name To Delete: ")

    for con in contacts:
        if name == con["name"]:
            contacts.remove(con)
            print("Contact deleted successfully.")
            return

    raise ContactNotFound("Contact is Not Found.")
        

def show_contact(contacts):
    print()
    print("Contacts:")
    for con in contacts:
        print(con["name"],":",con["number"])


while True:
    try:
        print("1.Add Contact.")
        print("2.Search Contact.")
        print("3.Delete Contact.")
        print("4.Show All Contact.")
        print("5.Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_contact()

        elif choice == 2:
            search_contact(contacts)

        elif choice == 3:
            delete_contact(contacts)

        elif choice == 4:
            show_contact(contacts)

        elif choice == 5:
            break
        else:
            print("Enter Valid Choice.")
        print("------------------------------")

    except ValueError:
        print("Enter Valid Number.")

    except ContactNotFound as e:
        print(e)

    

        

    

