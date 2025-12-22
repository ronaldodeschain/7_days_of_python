import httpx
from django.shortcuts import render
from googletrans import Translator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

async def listar_personagens(request):
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    translator = Translator()
    personagens_traduzidos = []

    # Use um cliente HTTP assíncrono
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
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

    context = {'personagens': personagens}

    # Pagination
    paginator = Paginator(personagens, 10) # Show 10 characters per page
    page = request.GET.get('page')
    try:
        personagens = paginator.page(page)
    except PageNotAnInteger:
    
        personagens = paginator.page(1)
    except EmptyPage:
    
        personagens = paginator.page(paginator.num_pages)

    context = {
    'personagens': personagens,
    'page': page
    }
    return render(request, 'app/personagens.html', context)