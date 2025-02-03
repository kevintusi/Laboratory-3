class Bank:
    def __init__(self):
        self._accounts = {}

    def __str__(self):
        """Return the string representation of the entire bank."""
        sorted_accounts = sorted(SavingsAccount.temp, key=lambda acc: self._accounts[acc].getName())
        return '\n'.join(map(str, [self._accounts[acc] for acc in sorted_accounts]))

    def add(self, account):
        """Inserts an account using its PIN as a key."""
        self._accounts[account.getPin()] = account

    def remove(self, pin):
        """Removes an account by its PIN and returns the removed account."""
        return self._accounts.pop(pin, None)

    def get(self, pin):
        """Returns an account by its PIN."""
        return self._accounts.get(pin, None)

    def computeInterest(self):
        """Computes interest for each account and returns the total."""
        total_interest = sum(account.computeInterest() for account in self._accounts.values())
        return total_interest

class SavingsAccount:
    """Represents a savings account with the owner's name, PIN, and balance."""
    RATE = 0.02
    temp = []

    def __init__(self, name, pin, balance=0.0):
        self._name = name
        self._pin = pin
        self._balance = balance
        SavingsAccount.temp.append(pin)

    def __str__(self):
        return f"Name:    {self._name}\nPIN:     {self._pin}\nBalance: {self._balance:.2f}"

    def getBalance(self):
        """Returns the account balance."""
        return self._balance

    def getName(self):
        """Returns the account holder's name."""
        return self._name

    def getPin(self):
        """Returns the account PIN."""
        return self._pin

    def deposit(self, amount):
        """Deposits the given amount and returns the new balance."""
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        """Withdraws the given amount. Returns None if successful, or an error message if unsuccessful."""
        if amount < 0:
            return 'Amount must be >= 0'
        elif self._balance < amount:
            return 'Insufficient funds'
        else:
            self._balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

def main():
    bank = Bank()
    bank.add(SavingsAccount("Vera", "1003", 59000.00))
    bank.add(SavingsAccount("Andrei", "1001", 4000.00))
    bank.add(SavingsAccount("Karyl", "1002", 1.00))
    bank.add(SavingsAccount("Kevin", "1004" , 100000))
    print(bank)

if __name__ == "__main__":
    main()