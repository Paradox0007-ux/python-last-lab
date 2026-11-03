
class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("\nName:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, name, acc_no, balance, interest):
        super().__init__(name, acc_no, balance)
        self.interest = interest

    def deposit(self, amount):
        print("\nSavings Account:")
        super().deposit(amount)

    def add_interest(self):
        interest_amount = self.get_balance() * self.interest / 100
        super().deposit(interest_amount)
        print("Interest Added:", interest_amount)

    def display(self):
        super().display()
        print("Interest Rate:", self.interest, "%")


class CurrentAccount(BankAccount):
    def __init__(self, name, acc_no, balance, limit):
        super().__init__(name, acc_no, balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount <= self.get_balance():
            super().withdraw(amount)
        elif amount <= self.get_balance() + self.limit:
            remaining = self.get_balance() + self.limit - amount
            super().withdraw(self.get_balance())
            self.deposit(remaining)
            print("Overdraft facility used!")
        else:
            print("Overdraft limit exceeded!")

    def display(self):
        super().display()
        print("Overdraft Limit:", self.limit)


accounts = []

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Display Accounts")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Add Interest")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        acc = input("Enter account number: ")
        balance = float(input("Enter balance: "))
        rate = float(input("Enter interest rate: "))

        accounts.append(SavingsAccount(name, acc, balance, rate))
        print("Savings Account Created!")

    elif choice == "2":
        name = input("Enter name: ")
        acc = input("Enter account number: ")
        balance = float(input("Enter balance: "))
        limit = float(input("Enter overdraft limit: "))

        accounts.append(CurrentAccount(name, acc, balance, limit))
        print("Current Account Created!")

    elif choice == "3":
        for account in accounts:
            account.display()

    elif choice in ("4", "5", "6"):
        acc = input("Enter account number: ")

        account = next(
            (a for a in accounts if a.acc_no == acc), None
        )

        if account is None:
            print("Account not found!")

        elif choice == "4":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "5":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "6":
            if isinstance(account, SavingsAccount):
                account.add_interest()
            else:
                print("Interest is only available for Savings Account!")

    elif choice == "7":
        print("Thank you for using Banking System!")
        break

    else:
        print("Invalid choice!")
