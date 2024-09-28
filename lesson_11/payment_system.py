from abc import ABC, abstractmethod
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
            print(f"Error cached: {error}")

    return inner


class PaymentProvider(ABC):
    def __init__(self, user: User):
        self.user: User = user
    
    @abstractmethod
    def authorize(self, **kwargs):
        pass

    @abstractmethod
    def checkout(self, Product):
        pass

    @abstractmethod
    def healthcheck(self):
        pass


class StripePaymentProvider(PaymentProvider):
    def authorize(self, **kwargs):
        token = kwargs.get("token", "")
        Stripe_API.authorize(
            token=token,
            user_email=self.user.email,
            card_number=self.user.card.number,
            expire_date=self.user.card.expire_date,
            cvv=self.user.card.cvv
        )
    
    def checkout(self, product: Product):
        Stripe_API.checkout(user_email=self.user.email, price=product.price)
        
    def healthcheck(self):
        if Stripe_API.healthcheck() is False:
            raise Exception("Stripe is not available")


class PaypalPaymentProvider(PaymentProvider):
    def authorize(self, **kwargs):
        username = kwargs.get("username", "")
        password = kwargs.get("password", "")
        PayPal_API.authorize(
            username=username,
            password=password,
            email=self.user.email,
            card_data=asdict(self.user.card),
        )

    def healthcheck(self):
        if PayPal_API.is_available() is False:
            raise Exception("Paypal is NOT AVAILABLE")

    def checkout(self, product:Product):
        PayPal_API.checkout(email=self.user.email, price=product.price)


def provider_dispatcher(name: str, user: User)-> PaymentProvider:
    if name == "stripe":
        return StripePaymentProvider(user=user)
    elif name == "paypal":
        return PaypalPaymentProvider(user=user)
    else:
        raise Exception(f"Provider {name} is not supported")
        
    
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

    stripe_credentials = {
        "token":  STRIPE_ACCESS_TOKEN
    }

    payment_provider: PaymentProvider = provider_dispatcher("stripe", john)
    try:
        payment_provider.healthcheck()
    except Exception as error:
        print(error)
    else:
        payment_provider.authorize(**stripe_credentials)
        payment_provider.checkout(samsung)

    payment_provider: PaymentProvider = provider_dispatcher("paypal", marry)
    try:
        payment_provider.healthcheck()
    except Exception as error:
        print(error)
    else:
        payment_provider.authorize(**PAYPAL_CREDENTIALS)
        payment_provider.checkout(iphone)


if __name__ == "__main__":
    main()
