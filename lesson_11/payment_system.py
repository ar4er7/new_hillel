from dataclasses import asdict
from .models import User, Product, Card
from .api import Stripe_API, PayPal_API


STRIPE_ACCESS_TOKEN = "4070b0df-e4f8-4a6f-b5bc-fa8293f8eb88"
PAYPAL_CREDENTIALS = {"username": "hillel", "password": "hillel123"}


def error_cather(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error cathed: {error}")

    return inner


@error_cather
def checkout(user: User, product: Product, payment_provider: str):
    if payment_provider == "stripe":
        Stripe_API.authorize(
            token=STRIPE_ACCESS_TOKEN,
            user_email=user.email,
            card_number=user.card.number,
            expire_date=user.card.expire_date,
            cvv=user.card.cvv,
        )
        Stripe_API.checkout(user_email=user.email, price=product.price)

    elif payment_provider == "paypal":
        PayPal_API.authorize(
            username=PAYPAL_CREDENTIALS["username"],
            password=PAYPAL_CREDENTIALS["password"],
            email=user.email,
            card_data=asdict(user.card),
        )
        PayPal_API.checkout(email=user.email, price=product.price)


def main():
    john = User(
        id=1,
        email="john@email.com",
        age=30,
        card=Card(number=5453010000095539, expire_date="12/25", cvv=300),
    )
    marry = User(
        id=2,
        email="mary@email.com",
        age=13,
        card=Card(number=5453010000095345, expire_date="10/25", cvv=312),
    )

    samsung = Product(name="Samsung", price=30_000)
    iphone = Product(name="Iphone", price=35_000)

    checkout(user=john, product=samsung, payment_provider="stripe")
    checkout(user=marry, product=iphone, payment_provider="paypal")


if __name__ == "__main__":
    main()
