from decimal import Decimal
from typing import Protocol



class PaymentService(Protocol):
    def process_payment(self, amount: Decimal) -> None:
        ...
        
    def process_payout(self, amount:Decimal) -> None:
        ...
