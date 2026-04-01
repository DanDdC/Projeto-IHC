from django.urls import path
from gekkoteca import views

urlpatterns = [
    path('', views.auth_view, name='auth'),      # Tela de Login/Cadastro
    path('home/', views.home_view, name='home'), # Tela Inicial
]