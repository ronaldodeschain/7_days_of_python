import asyncio
import requests
from pprint import pprint
from googletrans import Translator


url = "https://last-airbender-api.fly.dev/api/v1/characters"

async def main():
    personagens = (requests.get(url)).json()
    for personagem in personagens:
        translator = Translator()
        nome = await translator.translate(personagem.get('name', ''), dest='pt')
        afiliacao_original = personagem.get('affiliation', 'Nenhuma')
        afiliacao = await translator.translate(afiliacao_original, dest='pt')
        pprint(f"Nome: {nome.text}, Afiliação: {afiliacao.text}")

asyncio.run(main())
