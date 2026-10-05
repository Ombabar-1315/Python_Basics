import csv
import json


# ==============================
# Custom Exception
# ==============================

class InvalidExpenseError(Exception):
    pass


# ==============================
# Expense Class
# ==============================

class Expense:

    def __init__(self, title, amount, category, date):
        self.title = title
        self.__amount = 0
        self.category = category
        self.date = date

        # Use setter for validation
        self.amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value > 0:
            self.__amount = value
        else:
            raise InvalidExpenseError(
                "Amount must be greater than 0."
            )

    def show_expense(self):
        print("Title:", self.title)
        print("Amount:", self.amount)
        print("Category:", self.category)
        print("Date:", self.date)


# ==============================
# Online Expense
# ==============================

class OnlineExpense(Expense):

    def __init__(self, title, amount, category, date, platform):
        super().__init__(title, amount, category, date)
        self.platform = platform

    def show_expense(self):
        super().show_expense()
        print("Platform:", self.platform)


# ==============================
# Add Expense
# ==============================

expenses = []


def add_expense():

    try:
        title = input("Enter Expense Title: ")
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        date = input("Enter Date: ")

        while True:

            print("\nExpense Type:")
            print("1. Offline")
            print("2. Online")

            choice = int(input("Enter Choice: "))

            if choice == 1:

                expense = Expense(
                    title,
                    amount,
                    category,
                    date
                )

                expenses.append(expense)

                print("Expense Added Successfully.")
                break

            elif choice == 2:

                platform = input("Enter Platform: ")

                expense = OnlineExpense(
                    title,
                    amount,
                    category,
                    date,
                    platform
                )

                expenses.append(expense)

                print("Online Expense Added Successfully.")
                break

            else:
                print("Enter Valid Choice.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except InvalidExpenseError as e:
        print("Invalid Expense:", e)


# ==============================
# Display Expenses
# ==============================

def show_expenses():

    if not expenses:
        print("\nNo expenses available.")
        return

    print("\n========== ALL EXPENSES ==========")

    for i, expense in enumerate(expenses, start=1):

        print(f"\nExpense {i}")
        print("----------------")

        expense.show_expense()


# ==============================
# Calculate Total
# ==============================

def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense.amount

    return total


# ==============================
# Calculate Average
# ==============================

def calculate_average(expenses):

    if not expenses:
        return 0

    total = calculate_total(expenses)

    average = total / len(expenses)

    return average


# ==============================
# Find Highest Expense
# ==============================

def find_highest(expenses):

    if not expenses:
        return None, None

    highest = expenses[0]

    for expense in expenses:

        if expense.amount > highest.amount:
            highest = expense

    return highest.title, highest.amount


# ==============================
# Find Lowest Expense
# ==============================

def find_lowest(expenses):

    if not expenses:
        return None, None

    lowest = expenses[0]

    for expense in expenses:

        if expense.amount < lowest.amount:
            lowest = expense

    return lowest.title, lowest.amount


# ==============================
# Category Totals
# ==============================

def calculate_category_totals(expenses):

    category_totals = {}

    for expense in expenses:

        category = expense.category

        if category in category_totals:
            category_totals[category] += expense.amount

        else:
            category_totals[category] = expense.amount

    return category_totals


# ==============================
# Unique Categories
# ==============================

def unique_categories(expenses):

    categories = set()

    for expense in expenses:
        categories.add(expense.category)

    return categories


# ==============================
# *args Example
# ==============================

def calculate_amount(*amounts):

    total = 0

    for amount in amounts:
        total += amount

    return total


# ==============================
# **kwargs Example
# ==============================

def add_expense_details(**details):

    print("\nAdditional Expense Details:")

    for key, value in details.items():
        print(f"{key}: {value}")


# ==============================
# Show Analysis
# ==============================

def show_analysis():

    if not expenses:
        print("\nNo expenses available for analysis.")
        return

    total = calculate_total(expenses)
    average = calculate_average(expenses)

    high_name, high_amount = find_highest(expenses)
    low_name, low_amount = find_lowest(expenses)

    print("\n========== EXPENSE ANALYSIS ==========")

    print("Total Expense:", total)
    print("Average Expense:", round(average, 2))

    print("Highest Expense:", high_name)
    print("Highest Amount:", high_amount)

    print("Lowest Expense:", low_name)
    print("Lowest Amount:", low_amount)


# ==============================
# Category Analysis
# ==============================

def show_category_analysis():

    if not expenses:
        print("\nNo expenses available.")
        return

    category_totals = calculate_category_totals(expenses)
    categories = unique_categories(expenses)

    print("\n========== CATEGORY ANALYSIS ==========")

    print("\nCategory Totals:")

    for category, amount in category_totals.items():
        print(f"{category}: {amount}")

    print("\nUnique Categories:")

    for category in categories:
        print(category)


# ==============================
# Save CSV
# ==============================

def save_csv():

    try:

        with open(
            "expenses.csv",
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Title",
                "Amount",
                "Category",
                "Date",
                "Type",
                "Platform"
            ])

            for expense in expenses:

                if isinstance(expense, OnlineExpense):

                    expense_type = "Online"
                    platform = expense.platform

                else:

                    expense_type = "Offline"
                    platform = ""

                writer.writerow([
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.date,
                    expense_type,
                    platform
                ])

        print("Data saved successfully to expenses.csv.")

    except OSError as e:
        print("Error while saving CSV:", e)


# ==============================
# Save JSON Summary
# ==============================

def save_json():

    try:

        total = calculate_total(expenses)
        average = calculate_average(expenses)

        high_name, high_amount = find_highest(expenses)
        low_name, low_amount = find_lowest(expenses)

        category_totals = calculate_category_totals(expenses)

        summary = {
            "total_expense": total,
            "average_expense": average,
            "highest_expense": {
                "title": high_name,
                "amount": high_amount
            },
            "lowest_expense": {
                "title": low_name,
                "amount": low_amount
            },
            "category_totals": category_totals,
            "unique_categories": list(
                unique_categories(expenses)
            )
        }

        with open(
            "expenses.json",
            "w"
        ) as file:

            json.dump(
                summary,
                file,
                indent=4
            )

        print("Summary saved successfully to expenses.json.")

    except OSError as e:
        print("Error while saving JSON:", e)


# ==============================
# Read JSON
# ==============================

def read_json():

    try:

        with open(
            "expenses.json",
            "r"
        ) as file:

            data = json.load(file)

        print("\n========== SAVED JSON DATA ==========")

        print(json.dumps(
            data,
            indent=4
        ))

    except FileNotFoundError:
        print("expenses.json file not found.")

    except json.JSONDecodeError:
        print("Invalid JSON data.")


# ==============================
# Main Menu
# ==============================

print("=================================")
print("\t EXPENSE ANALYZER")
print("=================================")


while True:

    try:

        print("\n1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Analysis")
        print("4. Category Analysis")
        print("5. Save CSV")
        print("6. Save JSON")
        print("7. Read JSON")
        print("8. Show *args Example")
        print("9. Show **kwargs Example")
        print("10. Exit")

        choice = int(input("\nEnter Choice: "))

        if choice == 1:

            add_expense()

        elif choice == 2:

            show_expenses()

        elif choice == 3:

            show_analysis()

        elif choice == 4:

            show_category_analysis()

        elif choice == 5:

            save_csv()

        elif choice == 6:

            save_json()

        elif choice == 7:

            read_json()

        elif choice == 8:

            amount1 = float(input("Enter first amount: "))
            amount2 = float(input("Enter second amount: "))
            amount3 = float(input("Enter third amount: "))

            result = calculate_amount(
                amount1,
                amount2,
                amount3
            )

            print("Total:", result)

        elif choice == 9:

            add_expense_details(
                payment_method="Online",
                note="Food order",
                location="Home"
            )

        elif choice == 10:

            print("Thank you for using Expense Analyzer.")
            break

        else:

            print("Enter a valid choice.")

    except ValueError:

        print("Invalid input. Please enter a number.")