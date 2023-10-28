class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def calculate_interest(self):
        pass  

    def apply_transaction_fee(self):
        pass 

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        interest_rate = 0.03 
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Interest calculated. New balance: ${self.balance:.2f}")

class CheckingAccount(BankAccount):
    def apply_transaction_fee(self):
        transaction_fee = 1.0
        self.balance -= transaction_fee
        print(f"Transaction fee applied. New balance: ${self.balance:.2f}")

class BankCustomer:
    def __init__(self, name):
        self.name = name
        self.savings_account = None
        self.checking_account = None

    def create_savings_account(self, account_number, initial_balance=0):
        self.savings_account = SavingsAccount(account_number, initial_balance)
        print("Savings account created.")

    def create_checking_account(self, account_number, initial_balance=0):
        self.checking_account = CheckingAccount(account_number, initial_balance)
        print("Checking account created.")


customer = BankCustomer("John Doe")


customer.create_savings_account("SA123", 1000.0)
customer.savings_account.deposit(500.0)

customer.savings_account.calculate_interest()

customer.create_checking_account("CA456", 500.0)
customer.checking_account.deposit(300.0)


customer.checking_account.apply_transaction_fee()
