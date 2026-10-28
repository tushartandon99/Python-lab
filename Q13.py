class BankAccount:
    """Base class demonstrating encapsulation with private attributes."""
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"[{self.owner}] Deposited ${amount:.2f}. Balance: ${self.__balance:.2f}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"[{self.owner}] Withdrew ${amount:.2f}. Balance: ${self.__balance:.2f}")
            return True
        print(f"[{self.owner}] Withdrawal of ${amount:.2f} denied. Insufficient funds.")
        return False

    def get_balance(self):
        return self.__balance

    def _set_balance(self, amount):
        # Protected helper method to allow safe subclass modifications
        self.__balance = amount


class SavingsAccount(BankAccount):
    """Derived class extending functionality."""
    def __init__(self, owner, balance=0.0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"[{self.owner}] Applying {self.interest_rate*100}% interest.")
        self.deposit(interest)


class CurrentAccount(BankAccount):
    """Derived class demonstrating method overriding via super()."""
    def __init__(self, owner, balance=0.0, overdraft_limit=500.0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Method overriding to include overdraft logic
        if 0 < amount <= self.get_balance():
            return super().withdraw(amount)
        elif amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self._set_balance(new_balance)
            print(f"[{self.owner}] Overdraft used. Withdrew ${amount:.2f}. Balance: ${new_balance:.2f}")
            return True
        else:
            print(f"[{self.owner}] Withdrawal of ${amount:.2f} denied. Overdraft limit exceeded.")
            return False


def polymorphic_processor(accounts, withdrawal_amount):
    """Demonstrates a polymorphic interface handling multiple derived objects."""
    print(f"\n--- Batch Polymorphic Withdrawal: ${withdrawal_amount:.2f} ---")
    for acc in accounts:
        acc.withdraw(withdrawal_amount)


# === Execution/Testing ===
if __name__ == "__main__":
    # Instantiating objects
    savings = SavingsAccount("Alice", 1000)
    current = CurrentAccount("Bob", 200, overdraft_limit=300)

    # Class-specific methods
    savings.apply_interest()
    
    # Polymorphism in action
    account_list = [savings, current]
    
    polymorphic_processor(account_list, 400)
    polymorphic_processor(account_list, 150)