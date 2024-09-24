input_data = "100 UAH"

to_CHF_exchange: dict = {"UAH": 0.02, "USD": 0.84, "EUR": 0.93}


class Price:
    def __init__(self, value: int, currency: str) -> None:
        self.value = value
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Price):
            raise NotImplementedError

        if self.currency != other.currency:
            value_1 = self.value * to_CHF_exchange[self.currency]
            value_2 = other.value * to_CHF_exchange[other.currency]
            new_value = (value_1 + value_2) / to_CHF_exchange[self.currency]
        else:
            new_value = self.value + other.value

        return Price(new_value, self.currency)

    def __str__(self) -> str:
        return f"Value: {self.value}, {self.currency}"


Flight = Price(100, "UAH")
Train = Price(50, "USD")

total = Flight + Train

print(total)
