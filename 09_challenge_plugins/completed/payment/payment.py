from decimal import Decimal
from typing import Callable
import os
import importlib

PaymentHandlerFn = Callable[[Decimal], None]


# TODO build dynamically this list of payment methods
# PAYMENT_HANDLERS: dict[str, PaymentHandlerFn] = {
#     "cc": process_payment_cc,
#     "paypal": process_payment_paypal,
#     "apple": process_payment_apple_pay,
# }

path = os.path.dirname(__file__)
# keep only modules with payment methods
methods = [m.removesuffix(".py") for m in os.listdir(path) if not (m in ["payment.py"] or m.startswith("__"))]
modules = [importlib.import_module(f"payment.{m}") for m in methods]
funcs = [getattr(module, 'process_payment') for module in modules]

PAYMENT_HANDLERS = dict(zip(methods, funcs))


def handle_payment(total: Decimal) -> None:
    payment_type = input(
        f"What payment method would you like to use? ({'/'.join(PAYMENT_HANDLERS)}) "
    )

    if payment_type in PAYMENT_HANDLERS:
        # Process the payment
        PAYMENT_HANDLERS[payment_type](total)
    else:
        print(f"Payment type '{payment_type}' is not valid!")
