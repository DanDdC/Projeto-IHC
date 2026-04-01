from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse  # <-- NOVA IMPORTAÇÃO AQUI
from django.contrib import messages
from .models import Livraria, Livro, Colecao

def auth_view(request):
    return render(request, 'auth.html')

def home_view(request):
    livrarias = Livraria.objects.all()
    livros_aluguel = Livro.objects.all()
    colecoes = Colecao.objects.filter(ativa=True) 

    return render(request, 'home.html', {
        'livrarias': livrarias,
        'livros_aluguel': livros_aluguel,
        'colecoes': colecoes, # Envia para o HTML
    })

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

def add_carrinho(request, livro_id):
    if request.method == 'POST':
        livro = get_object_or_404(Livro, id=livro_id)
        tipo = request.POST.get('tipo_aquisicao', 'comprar')
        
        # Preço simulado de compra ou preço real de aluguel
        preco = 29.99 if tipo == 'comprar' else float(livro.preco_aluguel)
        
        # Inicia a sessão do carrinho se não existir
        if 'carrinho' not in request.session:
            request.session['carrinho'] = []
            
        # Adiciona o item ao carrinho
        request.session['carrinho'].append({
            'livro_id': livro.id,
            'titulo': livro.titulo,
            'autor': livro.autor,
            'tipo': 'Comprar' if tipo == 'comprar' else 'Alugar',
            'preco': preco,
            'capa_url': livro.capa.url if livro.capa else None
        })
        
        # Salva a sessão
        request.session.modified = True
        
        # ALTERAÇÃO AQUI: Em vez de redirecionar, devolvemos um JSON!
        return JsonResponse({'status': 'sucesso', 'mensagem': 'Item adicionado ao carrinho'})
    
    return redirect('home')

def carrinho_view(request):
    carrinho = request.session.get('carrinho', [])
    
    # Calcula o total
    total = sum(item['preco'] for item in carrinho)
    
    context = {
        'carrinho': carrinho,
        'total': total
    }
    return render(request, 'carrinho.html', context)

def pagamento_view(request):
    carrinho = request.session.get('carrinho', [])
    
    # Calcula os valores
    subtotal = sum(item['preco'] for item in carrinho)
    taxa_entrega = 15.20
    taxa_servico = 0.99
    total = subtotal + taxa_entrega + taxa_servico
    
    context = {
        'subtotal': subtotal,
        'taxa_entrega': taxa_entrega,
        'taxa_servico': taxa_servico,
        'total': total
    }
    return render(request, 'pagamento.html', context)

def limpar_carrinho_view(request):
    # Remove o carrinho da sessão se ele existir
    if 'carrinho' in request.session:
        del request.session['carrinho']
        request.session.modified = True
    return JsonResponse({'status': 'sucesso'})

def entrega_view(request):
    return render(request, 'entrega.html')

def livraria_detail_view(request, livraria_id):
    livraria = get_object_or_404(Livraria, id=livraria_id)
    
    # Como não temos categorias no modelo Livro ainda, vamos embaralhar
    # e dividir os livros existentes para simular as diferentes sessões do protótipo
    livros_recomendados = Livro.objects.order_by('?')[:4]
    livros_romance = Livro.objects.order_by('?')[:4]
    livros_hqs = Livro.objects.order_by('?')[:4]
    
    context = {
        'livraria': livraria,
        'livros_recomendados': livros_recomendados,
        'livros_romance': livros_romance,
        'livros_hqs': livros_hqs,
    }
    return render(request, 'livraria_detail.html', context) 
