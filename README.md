# 📚 GekkoTeca

**GekkoTeca** é um protótipo funcional de um aplicativo mobile focado no delivery, compra e aluguel de livros, conectando leitores a livrarias locais. 

Este projeto foi desenvolvido com foco em **Interação Humano-Computador (IHC)**. Em vez de ser apenas um design estático no Figma, a GekkoTeca foi codificada num ambiente web que simula perfeitamente a tela de um smartphone no navegador, oferecendo uma experiência tátil, responsiva e fluida de navegação ponta-a-ponta.

---

## 🎯 O Propósito do Protótipo
A ideia principal é trazer a facilidade e rapidez dos aplicativos de delivery de comida (como o iFood) para o mundo literário. O utilizador pode explorar coleções, pesquisar livros, verificar livrarias num mapa, adicionar itens ao carrinho e acompanhar a entrega.

Como se trata de um protótipo focado na **experiência do utilizador (UX)**, a persistência de dados de navegação (carrinho de compras e acervo pessoal) foi construída utilizando o sistema de **Sessões do Django**. Isso permite que qualquer pessoa teste o fluxo completo de compra sem a fricção de criar uma conta real num banco de dados.

---

## ✨ Funcionalidades Implementadas (Fluxo Completo)

O projeto possui diversas rotas interligadas que simulam um aplicativo real:

* **📱 Simulador Mobile CSS:** O frontend inteiro roda dentro de uma classe `.mobile-simulator`, com *scroll* interno e barra de navegação inferior (`bottom-nav`) fixa, garantindo a fidelidade do layout mobile em telas de PC.
* **🏠 Home e Carrosséis:** Página inicial dinâmica com banners de coleções, filtros de categorias e prateleiras de livros utilizando *Scroll Snap* horizontal.
* **🔍 Sistema de Busca:** Rota de pesquisa (`search_view`) para encontrar títulos e livrarias rapidamente.
* **🏪 Exploração de Livrarias:** Páginas de detalhes (`livraria_detail.html`) que mostram informações da loja (avaliação, distância) e o seu catálogo dividido por categorias (Recomendados, Romance, HQs).
* **📖 Detalhes do Livro:** Página dedicada a cada obra (`livro.html`) permitindo ao utilizador escolher entre **Comprar** ou **Alugar**.
* **🛒 Carrinho & Checkout Dinâmico:** Uso de *Fetch API* no Javascript para adicionar livros ao carrinho sem recarregar a página. A rota de pagamento (`pagamento_view`) calcula automaticamente o subtotal, taxa de entrega e taxa de serviço.
* **🚚 Acompanhamento de Pedido:** Tela de status de entrega interativa após a finalização da compra (`entrega.html`).
* **📚 Meu Acervo Inteligente:** Uma estante virtual (`acervo.html`) que lê a sessão do utilizador e, após o checkout, organiza automaticamente as aquisições nas prateleiras de "Comprados" e "Alugados".

---

## 🛠️ Tecnologias e Arquitetura

O projeto adota um padrão de arquitetura Model-Template-View (MTV) robusto e preparado para deploy em produção.

**Backend:**
* **Python 3.10+**
* **Django 5.1.x** - Framework principal responsável pelas rotas e renderização do lado do servidor.
* **Sessões Django (`request.session`)** - Utilizadas para manter o estado do carrinho e do acervo temporário.
* **SQLite3** - Banco de dados leve configurado com os modelos `Livraria`, `Livro` e `Colecao`.

**Frontend:**
* **HTML5 & CSS3** - Design construído do zero (sem frameworks externos) com variáveis CSS nativas, Flexbox avançado e ocultação de barras de *scroll* para uma imersão mobile perfeita.
* **JavaScript (Vanilla)** - Gestão de requisições assíncronas (Ajax/JSON) para o carrinho de compras.

**Segurança e Produção:**
* Otimização de entrega de ficheiros estáticos e de mídia (`STATIC_ROOT` e `MEDIA_ROOT`).
* Proteção de variáveis sensíveis utilizando variáveis de ambiente (`os.environ.get`) para ocultar a `SECRET_KEY` no repositório público.
* Deploy configurado e hospedado via **PythonAnywhere** (WSGI).

---

## 🚀 Como rodar o projeto localmente

Se deseja testar a GekkoTeca na sua própria máquina, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/Projeto-IHC.git](https://github.com/SEU_USUARIO/Projeto-IHC.git)
   cd Projeto-IHC

2. **Crie e ative um ambiente virtual:**
   ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

4. **Prepare o Banco de Dados e Ficheiros Estáticos:**
   ```bash
   python manage.py migrate
   python popular_banco.py  # Script para popular o banco de dados com dados fictícios
   python manage.py collectstatic

5. **Inicie o servidor local:**
   ```bash
   python manage.py runserver

6. **Acesse http://127.0.0.1:8000/ no seu navegador e aproveite a experiência!**

👨‍💻 Autoria e Créditos
Projeto arquitetado e desenvolvido por:  
Arhur Vitorino  
Daniel Donaire  
João Rafael Alcoforado  
Juan Riquelme  
Kelwin Karam  
Victor Carraly
