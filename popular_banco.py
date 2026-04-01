import os
import django

# Configura o ambiente do Django para o script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from gekkoteca.models import Livraria, Livro

def popular():
    print("A limpar dados antigos...")
    Livraria.objects.all().delete()
    Livro.objects.all().delete()

    print("A adicionar Livrarias...")
    Livraria.objects.create(
        nome="Livraria Aviaras",
        endereco="Rua Principal, 100",
        distancia_km=2.5,
        status_aberto=True
    )
    Livraria.objects.create(
        nome="Livraria Juquinha",
        endereco="Avenida Central, 200",
        distancia_km=1.5,
        status_aberto=True
    )
    Livraria.objects.create(
        nome="Livraria Tenebrosa",
        endereco="Beco Escuro, 13",
        distancia_km=4.1,
        status_aberto=True
    )

    print("A adicionar Livros...")
    # O campo 'capa' ficará em branco para que o seu template home.html 
    # utilize a imagem padrão de fallback (L_rezende.png) que já configurou.
    Livro.objects.create(titulo="O Colecionador", autor="John Fowles", preco_aluguel=15.90, capa="")
    Livro.objects.create(titulo="O Morro dos Ventos Uivantes", autor="Emily Brontë", preco_aluguel=12.50, capa="")
    Livro.objects.create(titulo="Wuthering Heights", autor="Emily Brontë", preco_aluguel=14.00, capa="")
    Livro.objects.create(titulo="A Culpa é das Estrelas", autor="John Green", preco_aluguel=18.00, capa="")
    Livro.objects.create(titulo="A Hipótese do Amor", autor="Ali Hazelwood", preco_aluguel=20.00, capa="")
    Livro.objects.create(titulo="De repente, o destino", autor="Desconhecido", preco_aluguel=16.50, capa="")

    print("Base de dados populada com sucesso!")

if __name__ == '__main__':
    popular()