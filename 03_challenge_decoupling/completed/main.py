from decimal import Decimal

from stripe_service import StripePaymentService
from bank import SavingsAccount, CheckingAccount, BankService


def main() -> None:

    payment_service = StripePaymentService()
    payment_service.set_api_key("sk_test_1234567890")

    savings_account = SavingsAccount("SA001", Decimal("1000"), payment_service)
    checking_account = CheckingAccount("CA001", Decimal("500"), payment_service)

    bank_service = BankService()

    bank_service.deposit(Decimal("200"), savings_account)
    bank_service.deposit(Decimal("300"), checking_account)

    bank_service.withdraw(Decimal("100"), savings_account)
    bank_service.withdraw(Decimal("200"), checking_account)

    print(f"Savings Account Balance: {savings_account.balance}")
    print(f"Checking Account Balance: {checking_account.balance}")


if __name__ == "__main__":
    main()
