import requests

request = requests.get('https://api.coincap.io/v2/assets')

data = request.json()

coins = data['data']

for coin in coins:
    for key in coin:
        print(f'{key}: {coin[key]}')