from decimal import Decimal
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Iterable


class OrderType(StrEnum):
    ONLINE = "online"
    IN_STORE = "in store"


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Order:
    id: int
    type: OrderType
    customer_email: str
    items: list[Item] = field(default_factory=list)

    def calculate_total_price(self) -> Decimal:
        return Decimal(sum(item.price for item in self.items))

    def calculate_discounted_price(self, discount: Decimal) -> Decimal:
        total_price = self.calculate_total_price()
        return total_price - total_price * discount
    
    def process(self):
        print(f"Processing {self.type} order...")
        print(generate_order_confirmation_email(self))
        match self.type:
            case OrderType.ONLINE:
                print("Shipping the order...")
                print(generate_order_shipping_notification(self))
            case OrderType.IN_STORE:
                print("Order ready for pickup.")
            case _:
                raise ValueError(f"Unknown order type: {self.type}")
        print("Order processed successfully.")

@dataclass
class Email:
    body: str
    subject: str
    recipient: str
    sender: str


def generate_order_confirmation_email(order: Order) -> Email:
    return Email(
        body=f"Thank you for your order! Your order #{order.id} has been confirmed.",
        subject="Order Confirmation",
        recipient=order.customer_email,
        sender="sales@webshop.com",
    )


def generate_order_shipping_notification(order: Order) -> Email:
    return Email(
        body=f"Good news! Your order #{order.id} has been shipped and is on its way.",
        subject="Order Shipped",
        recipient=order.customer_email,
        sender="sales@webshop.com",
    )



def main() -> None:
    items = [
        Item(name="T-Shirt", price=Decimal("19.99")),
        Item(name="Jeans", price=Decimal("49.99")),
        Item(name="Shoes", price=Decimal("79.99")),
    ]

    online_order = Order(
        id=123, type=OrderType.ONLINE, customer_email="sarah@gmail.com", items=items
    )

    total_price = online_order.calculate_total_price()
    print("Total price:", total_price)

    # ? dicounted_price = order.discounted_price
    discounted_price = online_order.calculate_discounted_price(Decimal("0.1"))
    print("Discounted price:", discounted_price)

    # ? order.process
    online_order.process()

    in_store_order = Order(
        id=456, type=OrderType.IN_STORE, customer_email="john@gmail.com"
    )

    in_store_order.process()


if __name__ == "__main__":
    main()
