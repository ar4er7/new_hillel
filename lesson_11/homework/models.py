from dataclasses import dataclass
import datetime
from abc import ABC, abstractmethod


@dataclass
class Post:
    message: str
    timestamp: datetime


class SocialChannel(ABC):
    def __init__(self, type_: str, followers: int):
        self.type_: str = type_
        self.followers: int = followers

    def post(self, post: Post):
        print(f'posting a message "{post.message}" into the {self.type_}')
