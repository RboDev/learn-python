from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)

    def __str__(self) -> str:
        lines : list[str] = []
        lines += ["Shopping Cart:"]
        lines += [f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}"]
        for item in self.items:
            total_price = item.price * item.quantity
            lines += [f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${total_price:>7.2f}"]

        lines += ["=" * 40]
        lines += [f"Total: ${self.calculate_total():>7.2f}"]

        return "\n".join(lines)
    
    def get_item(self, n:int) -> Item :
        if not (0 <= n < len(self.items)):
            raise ValueError("Index out of bound")
        else:
            return self.items[n]

    def update_item_price(self, n:int, new_price:Decimal):
        item = self.get_item(n)
        item.price = new_price

    def update_item_qty(self, n:int, new_qty:int):
        item = self.get_item(n)
        item.quantity = new_qty

    def remove_item(self, n:int):
        item = self.get_item(n)
        self.items.remove(item)

def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.5"), 10),
            Item("Banana", Decimal("2"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )

    # Update some items' quantity and price
    #cart.items[0].quantity = 10
    cart.update_item_qty(0,10)
    #cart.items[2].price = Decimal("3.50")
    cart.update_item_price(2, Decimal("3.50"))

    # Remove an item
    cart.remove_item(1)

    # Print the cart
    print(cart)

if __name__ == "__main__":
    main()
