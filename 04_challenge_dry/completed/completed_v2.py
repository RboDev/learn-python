from decimal import Decimal
from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Order:
    id: int
    customer_email: str
    items: list[Item] = field(default_factory=list)

    def calculate_total_price(self) -> Decimal:
        return Decimal(sum(item.price for item in self.items))

    def calculate_discounted_price(self, discount: Decimal) -> Decimal:
        total_price = self.calculate_total_price()
        return total_price - total_price * discount
    
    def process(self):
        print(generate_order_confirmation_email(self))


class OnlineOrder(Order):

    def process(self):
        print(f"Processing online order...")
        super().process()
        print("Shipping the order...")
        print(generate_order_shipping_notification(self))
        print("Order processed successfully.")

class InstoreOrder(Order):

    def process(self):
        print(f"Processing in store order...")
        super().process()
        print("Order ready for pickup.")
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

    online_order = OnlineOrder(
        id=123, customer_email="sarah@gmail.com", items=items
    )

    total_price = online_order.calculate_total_price()
    print("Total price:", total_price)

    # ? dicounted_price = order.discounted_price
    discounted_price = online_order.calculate_discounted_price(Decimal("0.1"))
    print("Discounted price:", discounted_price)

    # ? order.process
    online_order.process()

    in_store_order = InstoreOrder(
        id=456, customer_email="john@gmail.com"
    )

    in_store_order.process()


if __name__ == "__main__":
    main()
