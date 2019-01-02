import requests

# Do you wonder 1 EUR how many TRY or USD
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=TRY
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD

url="https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD"

response=requests.get(url)
print(response)                         # <Response [200]>

json_data=response.json()
print(json_data)                        # {'rates': {'USD': 1.145}, 'base': 'EUR', 'date': '2018-12-31'}
print(json_data['rates'])               # {'USD': 1.145}
print(json_data['rates']['USD'])        # 1.145


url="https://api.exchangeratesapi.io/latest?base=EUR&symbols=TRY"
response=requests.get(url)
print(response)                         # <Response [200]>

json_data=response.json()
print(json_data)                        # {'rates': {'TRY': 6.0588}, 'base': 'EUR', 'date': '2018-12-31'}
print(json_data['rates'])               # {'TRY': 6.0588}
print(json_data['rates']['TRY'])        # 6.0588
