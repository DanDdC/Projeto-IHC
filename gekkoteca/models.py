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
    
class Colecao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Coleção")
    imagem = models.ImageField(upload_to='colecoes/', blank=True, null=True, verbose_name="Imagem do Banner")
    ativa = models.BooleanField(default=True, verbose_name="Mostrar na Home?")

    class Meta:
        verbose_name = 'Coleção'
        verbose_name_plural = 'Coleções'

    def __str__(self):
        return self.nome