import requests
import json

url = "https://last-airbender-api.fly.dev/api/v1/characters"
response = requests.get(url)
dados = response.json()
for data in dados:
    print(f'{data['name']}\n')


