from dataclasses import dataclass, field
from decimal import Decimal
from typing import Callable



DISCOUNTS: dict[str, Callable[[Decimal], Decimal]] = {
    "SAVE10": (lambda x: x * Decimal("0.1")),
    "5BUCJSOFF": (lambda _:  Decimal("5.00")),
    "FREESHIPPING": (lambda _:  Decimal("2.00")),
    "BLKFRIDAY": (lambda x: x * Decimal("0.2")),
    "": (lambda _: Decimal("0.00"))
}


class ItemNotFoundException(Exception):
    pass


class DiscountCodeNotFoundException(Exception):
    ...


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str = ""

    def __post_init__(self):
        self.apply_discount(self.discount_code)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item:
        for item in self.items:
            if item.name == item_name:
                return item
        raise ItemNotFoundException(f"Item '{item_name}' not found.")

    @property
    def subtotal(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))

    def apply_discount(self, discount_code: str) -> None:
        if discount_code not in DISCOUNTS.keys():
            raise DiscountCodeNotFoundException(
                f"Code '{discount_code}' not found.")
        self.discount_code = discount_code

    @property
    def discount(self) -> Decimal:
        return DISCOUNTS[self.discount_code](self.subtotal)

    @property
    def total(self) -> Decimal:
        return self.subtotal - self.discount

    def display(self) -> None:
        # Print the cart
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}"
            )
        print("=" * 40)
        print(f"Subtotal: ${self.subtotal:>7.2f}")
        if self.discount:
            print(f"Discount: ${self.discount:>7.2f}")
        print(f"Total:    ${self.total:>7.2f}")


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
        discount_code="SAVE10",
    )

    cart.display()


if __name__ == "__main__":
    main()
