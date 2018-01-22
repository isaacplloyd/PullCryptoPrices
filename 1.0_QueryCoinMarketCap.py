import json
from urllib.request import urlopen

with urlopen('https://api.coinmarketcap.com/v1/ticker/?limit=50') as source:
    response = source.read()
    json_data = json.loads(response)

for currency in json_data:
    if currency['symbol'] == 'LTC':
        print ('LTC: $',currency['price_usd'])
    if currency['symbol'] == 'XMR':
        print('XMR: $', currency['price_usd'])
    if currency['symbol'] == 'BTC':
        print('BTC: $', currency['price_usd'])
    if currency['symbol'] == 'SC':
        print('SC: $', currency['price_usd'])
