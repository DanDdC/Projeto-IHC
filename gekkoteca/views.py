from django.shortcuts import render, get_object_or_404
from .models import Livraria, Livro

def auth_view(request):
    return render(request, 'auth.html')

def home_view(request):
    # Pega as livrarias em ordem aleatória
    livrarias = Livraria.objects.order_by('?')
    
    # Pega 6 livros de forma aleatória
    livros_aluguel = Livro.objects.order_by('?')[:6]
    
    context = {
        'livrarias': livrarias,
        'livros_aluguel': livros_aluguel
    }
    return render(request, 'home.html', context)

def search_view(request):
    # Pega o termo pesquisado na URL (ex: ?q=Romance)
    query = request.GET.get('q', '')
    
    # Busca todas as livrarias e livros misturados para simular o layout
    livrarias = Livraria.objects.order_by('?')
    livros = Livro.objects.order_by('?')
    
    context = {
        'query': query,
        'livrarias': livrarias,
        'livros': livros,
    }
    return render(request, 'search.html', context)

def livro_view(request, livro_id):
    # Busca o livro no banco de dados pelo ID. Se não achar, mostra erro 404.
    livro = get_object_or_404(Livro, id=livro_id)
    
    context = {
        'livro': livro
    }
    return render(request, 'livro.html', context)
