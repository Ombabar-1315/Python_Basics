expenses = [
    {"name": "Food", "amount": 200},
    {"name": "Travel", "amount": 100},
    {"name": "Books", "amount": 500}
]


class InvalidAmount(Exception):
    pass


class InvalidChoice(Exception):
    pass


def add_expense():
    name = input("Enter Expense name: ")
    amount = int(input("Enter Amount: "))

    if amount <= 0:
        raise InvalidAmount("Amount cannot be Zero or Negative.")

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added Successfully.")


def show_expenses(expenses):
    for exp in expenses:
        print(exp["name"], ":", exp["amount"])


def total_expenses(expenses):
    total = 0

    for exp in expenses:
        total += exp["amount"]

    return total


while True:

    try:
        print("\n1. Add Expenses")
        print("2. Show Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = int(input("Enter Your Choice: "))

        # Choice must be between 1 and 4
        if choice < 1 or choice > 4:
            raise InvalidChoice("Enter a choice between 1 and 4.")

        if choice == 1:
            add_expense()

        elif choice == 2:
            show_expenses(expenses)

        elif choice == 3:
            print("Total Expense:", total_expenses(expenses))

        elif choice == 4:
            print("Thank you!")
            break

        print("--------------------------------")


    except ValueError:
        print("❌ Enter a valid number.")

    except KeyError:
        print("❌ Required dictionary key is missing.")

    except InvalidAmount as e:
        print("❌", e)

    except InvalidChoice as e:
        print("❌", e)