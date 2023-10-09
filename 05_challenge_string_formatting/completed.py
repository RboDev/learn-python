from dataclasses import dataclass
from decimal import Decimal


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

    # Print the cart
    print("Shopping Cart:")
    print(f"Item       Price     Qty    Total")
    for item in items:
        total_price = item.price * item.quantity
        print(f"{item.name:15} ${item.price:8.2f} {item.quantity:4d} ${total_price:6.2f}")
    print("=" * 40)
    print(f"Total: ${total}")


if __name__ == "__main__":
    main()
