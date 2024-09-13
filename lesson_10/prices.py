import requests
from dataclasses import dataclass

ALPHAVANTAGE_API_KEY = "MO31CNEF7DLKTRW1"
MIDDLE_CURRENCY = 'CHF'

# EXCHANGE_RATES = {
#     "CHF":{
#         "USD": 0.9,
#         "UAH": 0.02, 
#     },
#     "USD":{
#         "CHF": 1.1,
#         "UAH": 0.3, 
#     },
#     "UAH":{
#         "CHF": 3,
#         "USD": 38,
#     },
# }

@dataclass
class Price:
    value: int
    currency: str
    
    def __add__(self, other: "Price")->"Price":
        return self
    
    def __add__(self, other)->"Price":
        if self.currency == other.currency:
            return Price(value=(self.currency + other.currency), currency = self.currency)
        
        left_in_middle = convert(value=self.value, currency_from=self.currency, currency_to=MIDDLE_CURRENCY)
        right_in_middle = convert(value=other.value, currency_from=other.currency, currency_to=MIDDLE_CURRENCY)
        total_in_middle = left_in_middle + right_in_middle
        total_in_left: float = convert(value=total_in_middle, currency_from=MIDDLE_CURRENCY, currency_to= self.currency)
        return Price(value= total_in_left, currency = self.currency)
        
        
            
    
    
def convert(value: float, currency_from: str, currency_to: str)->float:
    # coefficient: float = EXCHANGE_RATES[currency_from][currency_to]
    responce: requests.Response = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={ALPHAVANTAGE_API_KEY}"
    )
    result: dict = responce.json()
    coefficient = float(result[ "Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    # {
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
    return value * coefficient
            
fligt = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="UAH")

total = fligt + hotel
print(total)
