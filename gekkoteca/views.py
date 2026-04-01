from django.shortcuts import render
from .models import Livraria, Livro

def auth_view(request):
    return render(request, 'auth.html')

def home_view(request):
    # Pega todas as livrarias e os 6 primeiros livros do banco de dados
    livrarias = Livraria.objects.all()
    livros_aluguel = Livro.objects.all()[:6]
    
    context = {
        'livrarias': livrarias,
        'livros_aluguel': livros_aluguel
    }
    return render(request, 'home.html', context)
