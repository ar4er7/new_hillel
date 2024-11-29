import random
import string

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


# create_random_string: Callable[[int], str] = lambda size: "".join(
#     [random.choice(string.ascii_letters) for _ in range(size)]
# )
def create_random_string(size: int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(size))


@app.get("/generate-article")
async def get_information():

    return {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }


@app.get("/fetch-market")
async def get_current_market_state():
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=UAH&apikey=MO31CNEF7DLKTRW1"

    # response: requests.Response = requests.get(url)
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)

    rate: str = response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    return {"rate": rate}
