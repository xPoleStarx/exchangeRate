import json
import requests

api_url = 'https://api.exchangerate.host/latest?base='

to_exchange_type = input("What currency do you want to exchange?: ")
to_exchange_type = to_exchange_type.upper()

exchange_type_to = input("What currency do you want to exchange to?: ")
exchange_type_to = exchange_type_to.upper()

currency = input("Enter the amount you want to exchange: ")

result = requests.get(api_url+to_exchange_type)
result = json.loads(result.text)
print("-------------------------------\ninstant exchange rate")
print(f"{to_exchange_type} = {result['rates'][exchange_type_to]}\n ------------result------------ \n"
      f"{float(currency)} {to_exchange_type}= {result['rates'][exchange_type_to]*float(currency)} ")