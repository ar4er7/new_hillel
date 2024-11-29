import random
import string
from datetime import datetime, timedelta

import httpx
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


def create_random_string(size: int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(size))


class Item(BaseModel):
    src_currency: str
    dest_currency: str


@app.post("/rate-check/")
async def get_rate_from_currencies(item: Item):
    global last_answer_time, total_price
    current_time = datetime.now()
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={item.src_currency}&to_currency={item.dest_currency}&apikey=MO31CNEF7DLKTRW1"

    if last_answer_time:
        if current_time - last_answer_time < timedelta(minutes=10):
            return {
                "Source": item.src_currency,
                "Destination": item.dest_currency,
                "CACHED_rate": total_price,
                "CACHED_time": last_answer_time.strftime("%X"),
            }

    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)

    rate: str = response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    total_price = rate
    last_answer_time = current_time
    return {
        "Source": item.src_currency,
        "Destination": item.dest_currency,
        "rate": total_price,
    }


@app.get("/generate-article")
async def get_information():

    return {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }
