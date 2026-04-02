document.addEventListener('DOMContentLoaded', () => {
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');

    const eyeOpen = `
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.644C3.67 8.55 7.3 \
          12a1 1.012 1.012 0 0 1 0 .644c1.634 3.772 5.266 3.772 9.964 0a1.012 1.012 0 0 1 0-.644" />
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
        </svg>
    `;
    const eyeClosed = `
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 \
          16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 \
          4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 \
          3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.243 4.243L9.878 9.878" />
        </svg>
    `;

    togglePasswordButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault(); // Impede o envio do formulário acidental

            // Encontra o input de senha que é "irmão" deste botão
            const inputPassword = this.parentElement.querySelector('input');
            
            if (inputPassword) {
                if (inputPassword.type === 'password') {
                    inputPassword.type = 'text';
                    this.innerHTML = eyeClosed; // Muda o ícone SVG (IHC: Feedback visual)
                } else {
                    inputPassword.type = 'password';
                    this.innerHTML = eyeOpen; // Volta o ícone SVG
                }
            }
        });
    });

    // ---- ELEMENTOS DE TROCA DE TELA ----
    const loginSection = document.getElementById('login-section');
    const registerSection = document.getElementById('register-section');
    const linkToRegister = document.getElementById('link-to-register');
    const linkToLogin = document.getElementById('link-to-login');

    if (linkToRegister && linkToLogin) {
        linkToRegister.addEventListener('click', (e) => {
            e.preventDefault();
            loginSection.classList.add('hidden');
            registerSection.classList.remove('hidden');
        });

        linkToLogin.addEventListener('click', (e) => {
            e.preventDefault();
            registerSection.classList.add('hidden');
            loginSection.classList.remove('hidden');
        });
    }

    // ---- LÓGICA DE CADASTRO ----
    const registerForm = document.getElementById('register-form');
    const regError = document.getElementById('register-error');

    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('reg-email').value;
            const senha = document.getElementById('reg-senha').value;
            const senhaConfirma = document.getElementById('reg-senha-confirma').value;

            regError.classList.add('hidden');

            if (senha !== senhaConfirma) {
                regError.innerText = 'As senhas não coincidem. Tente novamente.';
                regError.classList.remove('hidden');
                return;
            }

            localStorage.setItem('gekkoteca_user_email', email);
            localStorage.setItem('gekkoteca_user_senha', senha);
            window.location.href = '/home/';
        });
    }

    // ---- LÓGICA DE LOGIN ----
    const loginForm = document.getElementById('login-form');
    const loginError = document.getElementById('login-error');

    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('login-email').value;
            const senha = document.getElementById('login-senha').value;

            loginError.classList.add('hidden');

            const dbEmail = localStorage.getItem('gekkoteca_user_email');
            const dbSenha = localStorage.getItem('gekkoteca_user_senha');

            if (email === dbEmail && senha === dbSenha) {
                window.location.href = '/home/';
            } else {
                loginError.innerText = 'E-mail não encontrado ou senha incorreta.';
                loginError.classList.remove('hidden');
            }
        });
    }
    // ---- LÓGICA DE PESQUISA ----
    const categoryCards = document.querySelectorAll('.category-card');
    const searchInput = document.getElementById('search-input');

    // 1. Redirecionar ao clicar em um card de categoria
    if (categoryCards.length > 0) {
        categoryCards.forEach(card => {
            card.style.cursor = 'pointer'; 
            card.addEventListener('click', () => {
                const categoryName = card.querySelector('.category-name').innerText;
                // Redireciona para a nova rota de pesquisa passando a categoria na URL
                window.location.href = '/pesquisa/?q=' + encodeURIComponent(categoryName);
            });
        });
    }

    // 2. Redirecionar ao apertar enter na barra de pesquisa
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault(); // Evita que a página recarregue sozinha
                const query = this.value.trim();
                if (query) {
                    window.location.href = '/pesquisa/?q=' + encodeURIComponent(query);
                }
            }
        });
    }
    // LÓGICA DO CARROSSEL DE COLEÇÕES COM BOLINHAS
    const bannerGrid = document.getElementById('bannerGrid');
    const dots = document.querySelectorAll('#paginationDots .dot');

    if (bannerGrid && dots.length > 0) {
        const cards = bannerGrid.querySelectorAll('.banner-card');

        // Clicar na bolinha faz rolar para a imagem certa
        dots.forEach(dot => {
            dot.addEventListener('click', () => {
                const index = parseInt(dot.getAttribute('data-index'));
                if (cards[index]) {
                    const cardLeft = cards[index].offsetLeft;
                    const containerOffset = bannerGrid.offsetLeft;
                    const scrollPosition = cardLeft - containerOffset - (bannerGrid.clientWidth / 2) + (cards[index].clientWidth / 2);
                    
                    bannerGrid.scrollTo({
                        left: scrollPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Deslizar o ecrã atualiza a bolinha acesa
        bannerGrid.addEventListener('scroll', () => {
            let currentIndex = 0;
            let minDiff = Infinity;

            cards.forEach((card, index) => {
                const cardCenter = card.offsetLeft + (card.clientWidth / 2);
                const containerCenter = bannerGrid.scrollLeft + (bannerGrid.clientWidth / 2);
                const diff = Math.abs(cardCenter - containerCenter);

                if (diff < minDiff) {
                    minDiff = diff;
                    currentIndex = index;
                }
            });

            dots.forEach(dot => dot.classList.remove('active'));
            if (dots[currentIndex]) {
                dots[currentIndex].classList.add('active');
            }
        });
    }
});