# 
# There are 2 errors within this file.
# 

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
        else:
            self.balance -= amount
            print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: ${self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_deposit=0.0):
        if name in self.accounts:
            print(f"Error: An account for {name} already exists.")
        else:
            account = BankAccount(name, initial_deposit)
            print(f"Account for {name} created with balance: ${initial_deposit}")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)
        else:
            print(f"Error: Account for {name} not found.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            self.accounts[name].withdraw(amount)
        else:
            print(f"Error: Account for {name} not found.")

    def display_accounts(self):
        if not self.accounts:
            print("No accounts in the bank.")
        else:
            for account in self.accounts.values():
                account.display_info()


# Main Program

bank.create_account("Alice", 1000)
bank.create_account("Bob", 500)

print("\nInitial Account Info:")
bank.display_accounts()

print("\nTransactions:")
bank.deposit("Alice", 200)
bank.withdraw("Bob", 100)

print("\nFinal Account Info:")
bank.display_accounts()
