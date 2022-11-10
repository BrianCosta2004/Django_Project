from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme = lista_filmes[0]
    else:
        filme = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme}


def lista_filmes_alta(request):
    lista_filme = Filme.objects.all().order_by('-visualizacoes')
    return {"lista_filmes_alta": lista_filme}

