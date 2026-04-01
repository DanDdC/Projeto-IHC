from django.db import models
from django.contrib.auth.models import User

class Livraria(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    distancia_km = models.DecimalField(max_digits=4, decimal_places=1)
    imagem = models.ImageField(upload_to='livrarias/', null=True, blank=True)
    status_aberto = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capas/')
    preco_aluguel = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.titulo