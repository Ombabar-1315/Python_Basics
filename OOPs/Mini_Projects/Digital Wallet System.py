class DigitalWallet:
    total_wallets = 0

    def __init__(self, owner, wallet_id, balance, currency):
        self.owner = owner
        self.wallet_id = wallet_id
        self.currency = currency

        if DigitalWallet.validate_amount(balance):
            self.__balance = balance
            DigitalWallet.total_wallets += 1
        else:
            self.__balance = 0

    # Property
    @property
    def balance(self):
        return self.__balance

    # Setter
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Enter Valid Amount.")

    # Deposit
    def deposit(self, amount):
        if DigitalWallet.validate_amount(amount):
            self.balance += amount
            print("Amount Deposited Successfully.")
        else:
            print("Enter Valid Amount.")

    # Withdraw
    def withdraw(self, amount):
        if not DigitalWallet.validate_amount(amount):
            print("Enter Valid Amount.")

        elif self.balance >= amount:
            self.balance -= amount
            print("Amount Withdrawn Successfully.")

        else:
            print("Insufficient Balance.")

    # Static Method
    @staticmethod
    def validate_amount(amount):
        return amount > 0

    # Show wallet
    def show_wallet(self):
        print("\n----------------------------")
        print("Owner:", self.owner)
        print("Wallet ID:", self.wallet_id)
        print("Balance:", self.balance)
        print("Currency:", self.currency)
        print("----------------------------")

    # Class Method
    @classmethod
    def show_total_wallets(cls):
        return cls.total_wallets


# Creating wallets
w1 = DigitalWallet("Om", "w1", 1500, "INR")
w2 = DigitalWallet("Rudra", "w2", 500, "USD")

# Store wallets in list
walet = [w1, w2]


# Menu
while True:

    print("\n================================")
    print("\tDigital Wallet System")
    print("================================")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Wallet")
    print("4. Exit")

    try:
        wallet_id = input("Enter Wallet ID: ").strip()

        # Find wallet
        wallet = None

        for w in walet:
            if w.wallet_id == wallet_id:
                wallet = w
                break

        # Wallet not found
        if wallet is None:
            print("Wallet Not Found.")
            continue

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            amount = int(input("Enter Amount to Deposit: "))
            wallet.deposit(amount)

        elif choice == 2:
            amount = int(input("Enter Amount to Withdraw: "))
            wallet.withdraw(amount)

        elif choice == 3:
            wallet.show_wallet()

        elif choice == 4:
            print("Thank You!")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Enter a valid number.")

    else:
        print("Operation Completed Successfully.")

    finally:
        print("Program Is Executed.")