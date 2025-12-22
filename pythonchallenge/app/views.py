import httpx
from django.shortcuts import render
from googletrans import Translator


async def listar_personagens(request):
    api_url = "https://last-airbender-api.fly.dev/api/v1/characters"
    translator = Translator()
    personagens_traduzidos = []

    # Use um cliente HTTP assíncrono
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        personagens = response.json()
        
        for personagem in personagens:
            nome_original = personagem.get('name', '')
            afiliacao_original = personagem.get('affiliation', 'Nenhuma')

            # Use 'await' para as chamadas de tradução
            nome_traduzido_obj = await translator.translate(nome_original,
                                                            dest='pt')
            afiliacao_traduzida_obj = await translator.translate(
                afiliacao_original, dest='pt')
            
            personagem['nome_traduzido'] = nome_traduzido_obj.text
            personagem['afiliacao_traduzida'] = afiliacao_traduzida_obj.text
            personagem['photoUrl'] = personagem.get('photoUrl', '')
    context = {'personagens': personagens}
    return render(request, 'app/personagens.html', context)