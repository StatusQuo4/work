class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number not in self.accounts:
            account = BankAccount(account_number, account_holder, initial_balance)
            self.accounts[account_number] = account
            return True
        return False

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.get_balance()
        return None

    def perform_transaction(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)

        if from_account and to_account and amount > 0:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                return True
        return False


# Example Usage
if __name__ == "__main__":
    bank_system = BankingSystem()

    # Create accounts
    bank_system.create_account("12345", "Alice", 1000)
    bank_system.create_account("67890", "Bob", 500)

    # Check account balances
    print("Alice's balance:", bank_system.get_account_balance("12345"))
    print("Bob's balance:", bank_system.get_account_balance("67890"))

    # Perform a transaction
    bank_system.perform_transaction("12345", "67890", 200)

    # Check account balances after the transaction
    print("Alice's balance after transaction:", bank_system.get_account_balance("12345"))
    print("Bob's balance after transaction:", bank_system.get_account_balance("67890"))
