import requests

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=MO31CNEF7DLKTRW1" 
responce = requests.get(url)
print(responce.json())