import csv 
import json

class InvalidExpenseError(Exception):
    pass


class Expense:

    def __init__(self,title,amount,category,date):
        self.title = title
        self.__amount = amount
        self.category = category
        self.date = date
        self.amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,value):
        if value > 0:
            self.__amount = value
        else:
            raise InvalidExpenseError(
                "Amount must be greater than 0."
            )


    
    def show_expenses(self):
        print("Title: ",self.title)
        print("Amount: ",self.amount)
        print("Category: ",self.category)
        print("Date: ",self.date)

    # def calculate_price(self,quantity):
    #     total_price = self.amount * quantity
    #     return total_price  
    


class OnlineExpense(Expense):

    def __init__(self, title, amount, category, date,platform):
        super().__init__(title, amount, category, date)
        self.platform = platform


    def show_expenses(self):
         super().show_expenses()
         print("Platform: ",self.platform)




expenses = []

def add_expense(**details):
    try:

        title = input("Enter Expense Title: ")
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        date = input("Enter Date: ")

        while True:
                
                print("\nExpense Type:")
                print("1.Offline")
                print("2.Online")
            
                choice = int(input("Enter Choice."))
                if choice == 1:
                    expense = Expense(title, amount, category, date)
                    expenses.append(expense)
                    print("Expense Added Successfully.")
                    break

                elif choice == 2:
                    platform = input("Enter Platform: ")
                    expense = OnlineExpense(title, amount, category, date,platform)
                    expenses.append(expense)
                    print("Expense Added Successfully")
                    break

                else:
                    print("Enter Valid Choice.")

    except ValueError:
        print("Invalid input. Please enter a valid amount.")

    except InvalidExpenseError as e:
        print("Invalid Expense:",e)



def show_all_expense(expenses):
   if not expenses:
       print("\n No expenses availble.")
       return
   
   for exp in expenses:
       exp.show_expenses()
       print("--------------------------")
        
    

def calculate_total(expenses):
    total = 0
    for i in expenses:
        total  += i.amount

    return total


def calculate_average(expenses):
    total = calculate_total(expenses)
    number = len(expenses)

    average = total / number

    return average


def find_highest(expenses):
    if not expenses:
        return None, None
    
    high = expenses[0]
    high_name = ""

    for exp in expenses:
        if exp.amount > high:
            high = exp.amount
            high_name = exp.title

    return high_name,high


def find_lowest(expenses):

    if not expenses:
        return None, None
    
    low = expenses[0].amount
    low_name = expenses[0].title

    for exp in expenses:
        if exp.amount < low:
            low = exp.amount
            low_name = exp.title

    return low_name,low



def calculate_category_totals(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense.category
        amount = expense.amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


def unique_category(expenses):
    categories = set()

    for exp in expenses:
        categories.add(exp.category)

    return categories


def calculate_amount(*expenses):
    total = sum(expenses)
    return total


def add_expenses_details(**details):

    print("\nAdditional Expenses Details.")

    for key , value in details.items():
        print(f"{key}:{value}")


def show_analysis():

    if not expenses:
        print("\nNo expenses available for analysis.")
        return

    total = calculate_total(expenses)
    average = calculate_average(expenses)

    high_name , high_amount = find_highest(expenses)
    low_name , low_amount = find_lowest(expenses)

    print("\n================ Expenses Analysis =================")

    print("Total Expenses: ",total)
    print("Average Expenses: ",average)

    print("Highest Name: ",high_name)
    print("Highest Amount: ",high_amount)

    print("Lowest Name: ",low_name)
    print("Lowest amount: ",low_amount)


def show_category_analysis():
    if not expenses:
        print("\nNo expenses available.")
        return

    category_totals = calculate_category_totals(expenses)
    categories = unique_category(expenses)

    print("\n=========== CATEGORY ANALYSIS ================")

    print("\nCategory Totals:")

    for category, amount in category_totals.items():
        print(f"{category} : {amount}")

    print("\nUnique Categories.")

    for category in categories:
        print(category)



def save_csv():
    try:


         with open("expenses.csv","w",newline="") as file:
             writer = csv.writer(file)

             writer.writerow([
                 "Title",
                 "Amount",
                 "Category",
                 "Date",
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
                unique_category(expenses)
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

    
    
print("=================================")
print("\t Expense Analyzer ")
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


        choice = int(input("Enter Choice: "))
        if choice == 1:
            add_expense()

        elif choice == 2:
            show_all_expense()

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
            a = float(input("Enter first Amount: "))
            b = float(input("Enter second Amount: "))
            c = float(input("Enter third Amount: "))

            result = calculate_amount(a,b,c)
            print("Total :",result)

        elif choice == 9:
            add_expenses_details(
                payment_method = "Online",
                note = "Food Order",
                location = "Home"
            )           


        elif choice == 10:
             print("Thank you for using Expense Analyzer.")
             break


        else:
            print("Enter a valid choice.") 
   

    except ValueError:
         print("Invalid input. Please enter a number.")
