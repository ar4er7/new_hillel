from datetime import datetime
import requests

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=PUJMLUZVGHUKQ3PS" 
responce = requests.get(url)
print(responce.json())
print(datetime.now().strftime("%d/%m/%y at %H:%M:%S"))