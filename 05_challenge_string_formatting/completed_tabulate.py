from dataclasses import dataclass
from decimal import Decimal
import tabulate
tabulate.PRESERVE_WHITESPACE = True

@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int


def main():
    # Create a shopping cart
    items = [
        Item("Apple", Decimal("1.50"), 10),
        Item("Banana", Decimal("2.00"), 2),
        Item("Pizza", Decimal("11.90"), 5),
    ]

    total = sum(item.price * item.quantity for item in items)

    data = [[f"{item.name:20}",  f"${item.price:6.2f}", f"{item.quantity:6d}", f"${item.price * item.quantity:6.2f}" ] for item in items]
    data.append([tabulate.SEPARATING_LINE])
    data.append(["Total","","",f"${total:6.2f}"])

    print(tabulate.tabulate(data, headers=["Item", "Price", "Qty", "Total"]))

    print(Item.__annotations__.keys())


if __name__ == "__main__":
    main()
