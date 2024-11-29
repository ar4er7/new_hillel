import random
import string
from datetime import datetime, timedelta
from typing import Callable

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

last_answer_time = None
total_price = 0

create_random_string: Callable[[int], str] = lambda size: "".join(
    [random.choice(string.ascii_letters) for _ in range(size)]
)


class Item(BaseModel):
    src_currency: str
    dest_currency: str


@app.post("/rate-check/")
async def get_rate_from_currencies(item: Item):
    global last_answer_time, total_price
    current_time = datetime.now()
    if last_answer_time:
        if current_time - last_answer_time < timedelta(seconds=10):
            return {
                "CACHED_price": total_price,
                "CACHED_time": last_answer_time.strftime("%X"),
            }

    last_answer_time = current_time
    total_price = random.randint(1, 10)
    return {
        "total_price": total_price,
        "time": current_time.strftime("%X"),
        "last_request_time": last_answer_time.strftime("%X"),
    }


@app.get("/generate-article")
async def get_information():

    return {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }
