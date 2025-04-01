class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

# Example Usage
acc = BankAccount("123456789", 1000)
acc.deposit(500)   # Expected output: Deposited 500. New balance: 1500
acc.withdraw(300)  # Expected output: Withdrawn 300. New balance: 1200
acc.withdraw(2000) # Expected output: Insufficient balance!
acc.display()      # Expected output: Account Number: 123456789, Balance: 1200
