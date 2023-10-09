from dataclasses import dataclass
from decimal import Decimal
from payment_service import PaymentService


@dataclass
class Account:
    account_number: str
    balance: Decimal
    payment_service:PaymentService

    def deposit(self, amount:Decimal):
        self.payment_service.process_payment(amount)
        self.balance += amount

    def withdraw(self, amount:Decimal):
        self.payment_service.process_payment(amount)
        self.balance -= amount


class SavingsAccount(Account):

    def deposit(self, amount:Decimal):
        print(f"Depositing {amount} into Savings Account {self.account_number}.")
        super().deposit(amount)

    def withdraw(self, amount: Decimal):
        print(f"Withdrawing {amount} from Savings Account {self.account_number}.")
        super().withdraw(amount)
    
class CheckingAccount(Account):

    def deposit(self, amount:Decimal):
        print(f"Depositing {amount} into Checking Account {self.account_number}.")
        super().deposit(amount)

    def withdraw(self, amount: Decimal):
        print(f"Withdrawing {amount} from Checking Account {self.account_number}.")
        super().withdraw(amount)


class BankService:
    def deposit(self, amount: Decimal, account: Account) -> None:
        account.deposit(amount)

    def withdraw(self, amount: Decimal, account: Account) -> None:
        account.withdraw(amount)

