from dataclasses import dataclass

@dataclass
class Price:
    value: int
    currency: str
    

fligt = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="EUR")

