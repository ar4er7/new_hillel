import json
from dataclasses import dataclass
from datetime import datetime

import requests

ALPHAVANTAGE_API_KEY = "PUJMLUZVGHUKQ3PS"
MIDDLE_CURRENCY = "CHF"


@dataclass
class Price:
    value: float
    currency: str

    def __add__(self, other) -> "Price":
        if self.currency == other.currency:
            return Price(value=(self.value + other.value), currency=self.currency)

        left_in_middle = convert(
            value=self.value, currency_from=self.currency, currency_to=MIDDLE_CURRENCY
        )
        right_in_middle = convert(
            value=other.value, currency_from=other.currency, currency_to=MIDDLE_CURRENCY
        )
        total_in_middle = left_in_middle + right_in_middle
        total_in_left: float = convert(
            value=total_in_middle,
            currency_from=MIDDLE_CURRENCY,
            currency_to=self.currency,
        )
        return Price(value=total_in_left, currency=self.currency)


def convert(value: float, currency_from: str, currency_to: str) -> float:
    responce: requests.Response = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={ALPHAVANTAGE_API_KEY}"
    )
    result: dict = responce.json()
    # result: dict ={
    #     "Realtime Currency Exchange Rate": {
    #         "1. From_Currency Code": "USD",
    #         "2. From_Currency Name": "United States Dollar",
    #         "3. To_Currency Code": "UAH",
    #         "4. To_Currency Name": "Ukrainian Hryvnia",
    #         "5. Exchange Rate": "41.18550000",
    #         "6. Last Refreshed": "2024-09-13 15:54:17",
    #         "7. Time Zone": "UTC",
    #         "8. Bid Price": "41.18419000",
    #         "9. Ask Price": "41.18619000"
    #     }
    # }
    try:
        float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    except KeyError:
        print("something wrong with the API responce. The rate set to 0")
        coefficient: float = 0.0

    else:
        coefficient = float(
            result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        )

    results: dict = {
        "currency_from": currency_from,
        "currency_to": currency_to,
        "rate": coefficient,
        "timestamp": datetime.now().strftime("%d/%m/%y at %H:%M:%S"),
    }
    with open("lesson_10\\logs.json", "r+") as file:
        file.seek(0, 2)
        json.dump(results, file, sort_keys=True, indent=2)
        file.write("\n")

    return value * coefficient


fligt = Price(value=1500, currency="USD")
hotel = Price(value=2000, currency="UAH")

total = fligt + hotel
print(total)
