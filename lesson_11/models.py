from dataclasses import dataclass


@dataclass
class Card:
    number: int
    expire_date: str
    cvv: int


@dataclass
class User:
    id: str
    email: str
    age: int
    card: Card


@dataclass
class Product:
    name: str
    price: int
