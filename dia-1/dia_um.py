import requests
import json
from pprint import pprint

url = "https://last-airbender-api.fly.dev/api/v1/characters"

personagem = (requests.get(url)).json()

for personagem in personagem:
    nome = personagem.get('name','')
    afiliacao = personagem.get('affiliation','')
    print(f'{nome} afiliado a {afiliacao}')
