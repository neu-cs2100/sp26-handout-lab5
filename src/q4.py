"""
Please implement the class below according to the documentation.

This includes creating a new read-only property, which is a property that
can be read but not set.
"""

class BankAccount:
    """Stores a bank account balance, and allows depositing and withdrawing money."""

    def __init__(self, initial_balance_cents: int) -> None:
        """
        Starts the bank account with an initial balance.
        
        Args:
            initial_balance_cents (int): Number of cents in the initial balance
        
        Raises:
            ValueError: If the initial balance is zero or negative
        """
        if initial_balance_cents <= 0:
            raise ValueError("Initial balance cannot be zero or negative")
        self._balance_cents = initial_balance_cents
    
    # TODO: create a read-only property called balance that returns the current balance in cents
    
    def __str__(self) -> str:
        """Returns a string representation of the bank account."""
        dollars = self._balance_cents / 100
        return f"BankAccount(balance=${dollars:.2f})"
    
    def deposit(self, amount_cents: int) -> None:
        """
        Adds money to the account.

        Args:
            amount_cents (int): The amount to deposit in cents
        
        Raises:
            ValueError: If the deposit amount is zero or negative
        """
        # TODO: implement
        pass

    def withdraw(self, amount_cents: int) -> None:
        """
        Withdraws money from the account.

        Args:
            amount_cents (int): The amount to withdraw in cents

        Raises:
            ValueError: If the withdrawal amount exceeds the current balance
            ValueError: If the withdrawal amount is zero or negative
        """
        # TODO: implement
        pass
