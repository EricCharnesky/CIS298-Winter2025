import json

import requests
import os
import hashlib

from urllib3 import request

# bing prompt: python check if file exists


file_path = 'request.json'

if os.path.exists(file_path):
    with open('request.json') as request_file:
        data = json.loads(request_file.read())
else:
    public_key = '6ff4890eb465b07375f3e1b78a64f21e'
    with open('key.txt') as key_file:
        private_key = key_file.readline().strip()


    # bing prompt: python hashlib md5
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the string
    md5_hash.update(f'1{private_key}{public_key}'.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hash_result = md5_hash.hexdigest()

    request = requests.get(
        f'http://gateway.marvel.com/v1/public/comics?ts=1&apikey={public_key}&hash={hash_result}')

    data = request.json()

    request_cache = open('request.json', 'w')
    request_cache.write(json.dumps(data))
    request_cache.close()


print(data)
for key in data:
    print(f'{key}: {data[key]}')

comic_data = data['data']
for result in comic_data['results']:
    for key in result:
        print(f'{key}: {result[key]}')



# request = requests.get('https://api.coincap.io/v2/assets')
#
# data = request.json()
#
# coins = data['data']
#
# for coin in coins:
#     for key in coin:
#         print(f'{key}: {coin[key]}')