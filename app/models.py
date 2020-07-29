from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=255)
    principal = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=255)
    preparo = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome